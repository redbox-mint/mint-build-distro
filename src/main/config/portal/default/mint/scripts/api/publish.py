from com.googlecode.fascinator.common import JsonSimple
from com.googlecode.fascinator.portal.services import ScriptingServices
from com.googlecode.fascinator.spring import ApplicationContextProvider
from com.googlecode.fascinator.common import JsonObject
from com.googlecode.fascinator.common.storage import StorageUtils
from java.io import ByteArrayInputStream, ByteArrayOutputStream
from com.googlecode.fascinator.api.indexer import SearchRequest
from com.googlecode.fascinator.common.solr import SolrResult
from org.apache.commons.io import IOUtils
from java.lang import Exception
from java.lang.reflect import Method
from java.lang import StringBuilder, String
from java.util import ArrayList, HashMap
class PublishData:

    def __init__(self):
        pass

    def __activate__(self, context):

         try:
             self.log = context["log"]
             self.httpRequest = context["httpServletRequest"]
             self.sessionState = context["sessionState"]
             self.services = context["Services"]
             self.sessionState.set("username", "admin")

             publicationHandler = ApplicationContextProvider.getApplicationContext().getBean("publicationHandler")

             builder = StringBuilder()
             aux = ""
             reader = self.httpRequest.getReader()
             aux = reader.readLine()
             while aux is not None:
                 builder.append(aux)
                 aux =reader.readLine()

             requestJsonString = builder.toString()

             requestJson = JsonSimple(requestJsonString)
             self.log.error(requestJson.toString(True))
             
             publicationHandler.publishRecords(requestJson.getArray("records"))
             
             knownIdMap = HashMap()
             records = requestJson.getArray("records")
             for record in records:
		 self.log.error(JsonSimple(record).toString(True))
                 identifier = record.get("required_identifiers")[0].get("identifier")
	         oid = record.get("oid")
                 knownIdMap.put(identifier,self.getKnownIds(oid))
		 self.log.error(identifier)
		 self.log.error(knownIdMap.get(identifier).toString())
                 
             for record in records:
                 self.updateRelationships(record.get("oid"),record.get("required_identifiers")[0].get("identifier"),knownIdMap)
            
         except Exception, e:
             self.log.error("publishing failed",e)
         finally:
             self.sessionState.remove("username")
             
             
    def updateRelationships(self,oid,identifier, knownIdMap):
        digitalObject = StorageUtils.getDigitalObject(self.services.getStorage(), oid)
        metadataJsonPayload = digitalObject.getPayload("metadata.json")
        metadataJsonInstream = metadataJsonPayload.open()
        metadataJson = JsonSimple(metadataJsonInstream)
        metadataJsonPayload.close()
            
        relationships = metadataJson.getArray("relationships")
	if relationships is not None:
	   for knownIdPid in knownIdMap.keySet():          
            for knownId in knownIdMap.get(knownIdPid):
           	   for relationship in relationships:
                    if knownId == relationship.get("identifier"):
                        relationship.put("curatedPid",knownIdPid)
                        relationship.put("isCurated",True)
                        break
                    
        istream = ByteArrayInputStream(String(metadataJson.toString(True)).getBytes())
        StorageUtils.createOrUpdatePayload(digitalObject,"metadata.json",istream)
            
        
    def getKnownIds(self,oid):
        knownIds = None
	req = SearchRequest("storage_id:"+oid+" AND known_ids:[* TO *]")
        req.addParam("fq", "")
        req.setParam("sort", "last_modified desc, f_dc_title asc");
        out = ByteArrayOutputStream()
        self.services.indexer.search(req, out)
        self.__result = SolrResult(ByteArrayInputStream(out.toByteArray()))        
	if self.__result.getResults().size() > 0:
            knownIds = self.__result.getResults()[0].getList("known_ids")

        return knownIds		

            
