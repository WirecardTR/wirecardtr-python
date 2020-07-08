from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring

#Ortak Ödeme sayfası 3d ve 3d olmadan ödeme için Xml çağrısının yapıldığı alanı temsil eder.
#Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
#İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class WDTicketSale3DURLOrSaleUrlProxyRequest:
    ServiceType=""
    OperationType=""
    Token=""
    Price=""
    MPAY=""
    ErrorURL=""
    SuccessURL=""
    ExtraParam=""
    Description=""
    PaymentContent=""
    InstallmentOptions=""

    def execute(self, req,configs):     
        helper = Helper()
        result= HttpClient.post(configs.BaseUrl,self.convert_to_xml(req))
        return result

    def convert_to_xml(self,req):
        main_root=Element('WIRECARD')
        ServiceType=SubElement(main_root, 'ServiceType')
        ServiceType.text= req.ServiceType
        OperationType=SubElement(main_root,'OperationType')
        OperationType.text=req.OperationType
        MPAY=SubElement(main_root,'MPAY')
        MPAY.text=req.MPAY  
        Price=SubElement(main_root,'Price')
        Price.text=req.Price
        PaymentContent=SubElement(main_root,'PaymentContent')
        PaymentContent.text=req.PaymentContent
        ErrorURL=SubElement(main_root,'ErrorURL')
        ErrorURL.text=req.ErrorURL
        SuccessURL=SubElement(main_root,'SuccessURL')
        SuccessURL.text=req.SuccessURL 
        Description=SubElement(main_root,'Description')
        Description.text=req.Description
        ExtraParam=SubElement(main_root,'ExtraParam')
        ExtraParam.text=req.ExtraParam
        token_root=SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin  
        InstallmentOptions = SubElement(token_root, 'InstallmentOptions')
        InstallmentOptions.text = req.Token.InstallmentOptions     
        result = tostring(main_root).decode('utf-8')
        return (result)
