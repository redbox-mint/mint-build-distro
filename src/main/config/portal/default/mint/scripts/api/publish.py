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
from java.lang import StringBuilder
from java.util import ArrayList
class PublishData:

    def __init__(self):
        pass
    
    def __activate__(self, context):
         
         try:
             self.log = context["log"]

             self.response = context["response"]
             out = self.response.getPrintWriter("text/plain; charset=UTF-8")
             self.request = context["request"]
             self.httpRequest = context["httpServletRequest"]
             self.systemConfig = context["systemConfig"]
             self.storage = context["Services"].getStorage()
             self.indexer = context["Services"].getIndexer()
             self.sessionState = context["sessionState"]
             self.sessionState.set("username", "admin")
        
             out.close()
             publicationHandler = ApplicationContextProvider.getApplicationContext().getBean("publicationHandler")

             oid = self.request.getParameter("oid")
             
             builder = StringBuilder()
             aux = ""
             reader = self.httpRequest.getReader()
             aux = reader.readLine()
             while aux is not None:
                 builder.append(aux)
                 aux =reader.readLine()

             requestJsonString = builder.toString()

             requestJson = JsonSimple(requestJsonString)
             list = ArrayList()
             list.add(requestJson.getJsonObject())
             publicationHandler.publishRecords(list)
         except Exception, e:
        
             self.response.setStatus(500)
             #self.log.error("publishing failed",e)
         finally:
             self.sessionState.remove("username")
