from com.googlecode.fascinator.common import JsonSimple
from com.googlecode.fascinator.portal.services import ScriptingServices
from com.googlecode.fascinator.spring import ApplicationContextProvider
from com.googlecode.fascinator.common import JsonObject
from com.googlecode.fascinator.common.storage import StorageUtils
from java.io import ByteArrayInputStream, ByteArrayOutputStream
from com.googlecode.fascinator.api.indexer import SearchRequest
from com.googlecode.fascinator.common.solr import SolrResult
from org.apache.commons.io import IOUtils

class PublishData:

    def __init__(self):
        pass
    
    def __activate__(self, context):
         
         try:
             self.log = context["log"]
             self.response = context["response"]
             self.request = context["request"]
             self.systemConfig = context["systemConfig"]
             self.storage = context["Services"].getStorage()
             self.indexer = context["Services"].getIndexer()
             self.sessionState = context["sessionState"]
             self.sessionState.set("username", "admin")
        
             out = self.response.getPrintWriter("text/plain; charset=UTF-8")
             publicationHandler = ApplicationContextProvider.getApplicationContext().getBean("publicationHandler")

             oid = self.request.getParameter("oid")
             requestJsonString = IOUtils.toString(self.request.getReader())
             requestJson = JsonSimple(requestJsonString)
             list = ArrayList()
             list.add(requestJson.getJsonObject())
             publicationHandler.publishRecords(list)
         except:
             self.response.setStatus(500)
         finally:
             self.sessionState.remove("username")
