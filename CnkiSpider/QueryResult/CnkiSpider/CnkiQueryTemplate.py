from copy import deepcopy

queryUrl = "https://kns.cnki.net/KNS8/Brief/GetGridTableHtml"

cnkiHeaders = {
    "Host": "kns.cnki.net",
    "Connection": "keep-alive",
    "Content-Length": "6581",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "Accept": "text/html, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://kns.cnki.net",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://kns.cnki.net/kns8/AdvSearch?dbprefix=SCDB&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCVD%2CCJFN%2CCCJD",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "ASP.NET_SessionId=5ykwbltcra4fvgx5lv5ylk4n; SID_kns8=123117; cnkiUserKey=dfd0bd66-d5de-9db6-fe47-1bc3929f2995; Ecp_ClientId=2210529100501448113; Ecp_IpLoginFail=210529114.249.214.55; SID_kns_new=kns123123; CurrSortFieldType=desc; Ecp_ClientIp=114.249.214.55; SID_recommendapi=125143; SID_kcms=124107; ASPSESSIONIDACDRBQBD=AGMBMOHAKKCMKDBLGNPMCIOK; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); _pk_id=41eabffe-fb46-47da-bfd7-f061df24f40e.1622253926.3.1622266948.1622263543."
}

customModeFormDataTemplate = {
    "IsSearch": (None, "true"),
    "QueryJson": (None, """{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCVD,CJFN,CCJD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":4,"Items":[],"ChildItems":[{"Key":"input[data-tipid=gradetxt-1]","Title":"作者","Logic":0,"Items":[{"Key":"","Title":"这是作者的名字","Logic":1,"Name":"AU","Operate":"=","Value":"这是作者的名字","ExtendType":1,"ExtendValue":"中英文对照","Value2":""}],"ChildItems":[]},{"Key":"input[data-tipid=gradetxt-2]","Title":"作者单位","Logic":1,"Items":[{"Key":"","Title":"中国人民大学","Logic":1,"Name":"AF","Operate":"%","Value":"中国人民大学","ExtendType":1,"ExtendValue":"中英文对照","Value2":""}],"ChildItems":[]}]},{"Key":"ControlGroup","Title":"","Logic":1,"Items":[],"ChildItems":[]}]}}"""),
    "SearchSql": (None, "0645419CC2F0B23BC604FFC82ADF67C692F6944D0202D2DC6656A6C7AC1EDC809A155BF2DE12E2F98C4BD55B8DC0937B674DE0CD2B86BB3266824FC750BED96C00B6FFF8B53C732897B1E623A882A32F0BF5CF51B6EAB5042BB9034B07B74C7567AD9C4111D92A13DEE9BBC8802C0D282F61171EB1794B796728CBF9FEE654FB6C550FE2154E7B199FF2B0A2F14AFB850735D5697534FBB43620CC6627D49477153E142292C900AECEE9968C0C2D01B114E7D3A5C688C197F2D6353CEEA237DECD555EDDFE4641352CE4DE3CD5DB4ADF5126EB9AAB81EEB6A9C7048B3ABC508E2511FFECD5B809118E6FE24E065BDF56F8D679AD87AEC534278173EA90C7BD2F782DF316E0689F3F9CF7130A3D164C0B9F67E0BCFD40B11A893E059B385C139C93381B0E49D9B341E9F873F36CD7419DB9DCFAEE1BC089BBDD3F69BD336BCE0E0CB84C933EE6C249556E6F2832A7DBC426AC9B3FF7C49275C5C9A40BAEE1916D88FE3B89F46F3855840137991445DDDE36419A95CC34A3A67996D1066FC72587ECC3178EF9FE478D64E053B67FE75AF13E01C467EF6BB65CB74CBC667876B06414BBE808D9BFDE5C7B37665C52B788CE77B25BBF742357D34924C53618AAB0F1F923AD03D5C0AAD60B43CDF34DE9F2642F6432E1AE8588C458E5A4F89EA592507F2D75D75E5CFC0C5EC385E23CDDE479774AB9AA0C848545A87A13C88243D0F316BDD0D2D277F4156124D62AF5D1752EE9DF1AA61E73BD1851CA0CCBB0E643BBC465A5A252D0379F50BBCDD9057F7D9B5963318588BCA97EB74575AB118421EE8725A4E43DD27C107D64B1941DBCCB6E5126BC57C7E14BD5142219D1F0BCC312D76C5E166382E7A14D0D8212827A25ACD9BD083214B358CE6CF5DAD6A25B1B6D6513211C44E00F79B2862723CAC5828518BDDC3D1C4A4450501000B35D9173CD222F55DADD4BC7BB18D9AB47CE6299C5EC3F7B7BD795B65A1DB63746D7856CA667C6D0C28309D4176A54A771C8303BA11FC70D5FE03FE808B35150681CE1449249A6513EB94BE9DBE1002F0C41B2DC471CF1792524EDFEBC6BA3838E316B9FCF39E2F6DC7F08C6AF7C05DE1C44FD30BA2E7423256156E8E3F388E4069C0C2BB459C523134D5AF0CD59A6508A08A3F57F4BD33020E8A966326745D125A0599DE6710B72EC02E3A4C914207F9652A46A952710D24D86D42ED92C2C366727E97A13A4F495FCB3B07537A94EAA1BF1A29EB467F2F53042A8A74A590B5636DEF39E4E8A1E43617743BB24907B87DBD84C61D0A6F2475AEB9E541B0C4B446801E4FD8ACBAED1E7552A7735301749E63599FF0910F191473383338EE3F0A2CDC5CADB7DCC7A46065DC7C652185ECD579930A9F6E5B6F63ABA7283868365C8DC3E75D73A1B22FF62D7CF02FBB0B889D3F1B608E16B29829170DE0CE3B755F1E1DAABE2117B7D52BA44F2D615A436C2CCAE062EB78384486DBD8A3D510021BFC733621A0E51C8D44C892DDE003CD64B91ADCF8DEC5083E07CE303EB2C227636F3B0E69E45F866BCBCEED86318ECF8F3549C70C8DC88EC01D9722EFC2E7B1B295C85CE0A2BC0E30BCC6524B1911DFEE2008357E11A4C29F27C42831635581BD326FAE2AB9FEC74DE31A3B24DDBBC88E5AB175864FD51198762AE146D3286556F3F48D51F3B7F0153BCC6B7EB6D7B5A8F10B9134628CD3C6BE979DC26FAA476536DEB0B698E7A6F0A0CE2C8AFE58CC1AFBF821234E5D21F9B47B023257C14DD78FE096DFF136165BF9C2BCD5125A2393A3971592CAAEB0DC2A36E7EC40EF057080E5A29C48E4CCE2ACF786042AD4005433491CCC7D55A1F15575AB41D530C1F7FD19F28475C9C9A4548FE7C3E4298D460D882648C9A5F07172482123C39907BD9A885F16D29EACCFD03D27F87E9563E99A6C2C7E798E603561E97AE3CDBB185A7970E655C6016908654B7FCC8EDF36A5E2AC94ACBD29BD2A83C20C87C19CADB29BD5F61690A845FB6EB947DA23FECFFDD4F9139492EE149614DB54850E02374EA602B42C726A65DFDA81C54B2E027880B49CCE2D16607AA87C08EE0986FED8540FAF2761C44C208DA20D659C86777FD26498A3CACBC1C4270BAF96A001072AA7F7AEC171D1D3E514F27D957B885EF217A32C65565D765794A6CE877D442CBFA4562554C6CA73A4510A401BFFFD4923AA560C414750FDAD7420DEBEBF232B8E26A50308E29B8A238724B2D14AAA156E4145EB3A151A145A3012102CFC8CA4B46C54B2652F1D29CEA9F905CE25DF61012DD58ADE9EA3B6ED24E713229222EB39FA58DD73A4B7674304AB8B2784B6F627826F530C6B1F381A634E0FC0560BAAAA10275B8A0936E0CC385B1377764459D5695DA7DBB061574363AA79D8EDC1B322D0879DF89D6E77ACD922F22E6CAD8340A581D5403E8840817CD0AA07CE8AD202FB76691C4813A8231BDEEEF75CAC34BA184CA6CDE69D3F142B18F31BA50471BA6EDA17A0BE6BFF5F45D74982F859639775110016E95D0FDBA72FE7F352D132AC80A8C926AF008D15022D4CC35268E721919B89E6AF590DDAA397692058787D721B88E5D464876B867E84593A1F4F336606B026BC4DA7AFC7C985208BE09C4097D2315813C353A6E37C13A4CF459A97D78D90C882B1D3B29701560CFCE5B2EDE98D7B6BFD015115C4CF71F4FB3BD65282B3F46C349C2A214319C734C7EC3D8BCEB3F014228511F7CAB7F3BAAE56364BA0862FAFB5FD2976C6F922357B42D01899DE2CC26E9752BD0BAA6675BF07FF413835661C2BCF72F643AC14F7767FF21F9A37D2BF7B5765E18A4D58953D7C0EF90BD0E502E3D9A27951BCD476CD8D7EAA8A58604B2D70E49D26C7B3D91CDCDE527BE5552FF2641CA590E0C4DA0FEA2B674B8F968039C64829BD66BC74E3530A64865D75A23BFBE33E5894AA4BBE8E97EFD92BFE4C9C00179CC76CF13EB0998C444746AEC18306A301C936623E2030355E0D00D7A40B6DB574E23E577F49C5A4BB949B4F936FD2F9DFC1709D5293C2F9A215E96AF000E6288C2534CC988F976C4EDD1092424D017D03D7707A7E3A1763C16A08701124748819A36487DE86A46D5357AD35ED944C3EEA7C1E538614B11EC919DCCBB50A27382F0A61905F99FFAD819F7A97B57EA50E509991FEE6714B924B74722BABE7AEA483EFFC7E16C0791932EAB66A38D16F5408E08912E9A833A908AA9812ED16BE270EDBB0A704A7E66C133A3CB7ED0886A7B43FBA5939CB39B8D2AB469311F4249D7E7E946AFA7FB37DD52ED9373B21E7D7E674939670C95B54B"),
    "PageName": (None, "DefaultResult"),
    "HandlerId": (None, "0"),
    "DBCode": (None, "SCDB"),
    "KuaKuCodes": (None, "CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCVD,CJFN,CCJD"),
    "CurPage": (None, "1"),
    "RecordsCntPerPage": (None, "50"),
    "CurDisplayMode": (None, "custommode"),
    "CurrSortField": (None, "%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)"),
    "CurrSortFieldType": (None, "desc"),
    "IsSortSearch": (None, "false"),
    "IsSentenceSearch": (None, "false"),
    "Subject": (None, )
}

listModeFormDataTemplate = {
    "IsSearch": (None, "true"),
    "QueryJson": (None, """{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCVD,CJFN,CCJD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":4,"Items":[],"ChildItems":[{"Key":"input[data-tipid=gradetxt-1]","Title":"作者","Logic":0,"Items":[{"Key":"","Title":"这是作者的名字","Logic":1,"Name":"AU","Operate":"=","Value":"这是作者的名字","ExtendType":1,"ExtendValue":"中英文对照","Value2":""}],"ChildItems":[]},{"Key":"input[data-tipid=gradetxt-2]","Title":"作者单位","Logic":1,"Items":[{"Key":"","Title":"中国人民大学","Logic":1,"Name":"AF","Operate":"%","Value":"中国人民大学","ExtendType":1,"ExtendValue":"中英文对照","Value2":""}],"ChildItems":[]}]},{"Key":"ControlGroup","Title":"","Logic":1,"Items":[],"ChildItems":[]}]}}"""),
    "SearchSql": (None, "0645419CC2F0B23BC604FFC82ADF67C692F6944D0202D2DC6656A6C7AC1EDC809A155BF2DE12E2F98C4BD55B8DC0937B674DE0CD2B86BB3266824FC750BED96C00B6FFF8B53C732897B1E623A882A32F0BF5CF51B6EAB5042BB9034B07B74C7567AD9C4111D92A13DEE9BBC8802C0D282F61171EB1794B796728CBF9FEE654FB6C550FE2154E7B199FF2B0A2F14AFB850735D5697534FBB43620CC6627D49477153E142292C900AECEE9968C0C2D01B114E7D3A5C688C197F2D6353CEEA237DECD555EDDFE4641352CE4DE3CD5DB4ADF5126EB9AAB81EEB6A9C7048B3ABC508E2511FFECD5B809118E6FE24E065BDF56F8D679AD87AEC534278173EA90C7BD2F782DF316E0689F3F9CF7130A3D164C0B9F67E0BCFD40B11A893E059B385C139C93381B0E49D9B341E9F873F36CD7419DB9DCFAEE1BC089BBDD3F69BD336BCE0E0CB84C933EE6C249556E6F2832A7DBC426AC9B3FF7C49275C5C9A40BAEE1916D88FE3B89F46F3855840137991445DDDE36419A95CC34A3A67996D1066FC72587ECC3178EF9FE478D64E053B67FE75AF13E01C467EF6BB65CB74CBC667876B06414BBE808D9BFDE5C7B37665C52B788CE77B25BBF742357D34924C53618AAB0F1F923AD03D5C0AAD60B43CDF34DE9F2642F6432E1AE8588C458E5A4F89EA592507F2D75D75E5CFC0C5EC385E23CDDE479774AB9AA0C848545A87A13C88243D0F316BDD0D2D277F4156124D62AF5D1752EE9DF1AA61E73BD1851CA0CCBB0E643BBC465A5A252D0379F50BBCDD9057F7D9B5963318588BCA97EB74575AB118421EE8725A4E43DD27C107D64B1941DBCCB6E5126BC57C7E14BD5142219D1F0BCC312D76C5E166382E7A14D0D8212827A25ACD9BD083214B358CE6CF5DAD6A25B1B6D6513211C44E00F79B2862723CAC5828518BDDC3D1C4A4450501000B35D9173CD222F55DADD4BC7BB18D9AB47CE6299C5EC3F7B7BD795B65A1DB63746D7856CA667C6D0C28309D4176A54A771C8303BA11FC70D5FE03FE808B35150681CE1449249A6513EB94BE9DBE1002F0C41B2DC471CF1792524EDFEBC6BA3838E316B9FCF39E2F6DC7F08C6AF7C05DE1C44FD30BA2E7423256156E8E3F388E4069C0C2BB459C523134D5AF0CD59A6508A08A3F57F4BD33020E8A966326745D125A0599DE6710B72EC02E3A4C914207F9652A46A952710D24D86D42ED92C2C366727E97A13A4F495FCB3B07537A94EAA1BF1A29EB467F2F53042A8A74A590B5636DEF39E4E8A1E43617743BB24907B87DBD84C61D0A6F2475AEB9E541B0C4B446801E4FD8ACBAED1E7552A7735301749E63599FF0910F191473383338EE3F0A2CDC5CADB7DCC7A46065DC7C652185ECD579930A9F6E5B6F63ABA7283868365C8DC3E75D73A1B22FF62D7CF02FBB0B889D3F1B608E16B29829170DE0CE3B755F1E1DAABE2117B7D52BA44F2D615A436C2CCAE062EB78384486DBD8A3D510021BFC733621A0E51C8D44C892DDE003CD64B91ADCF8DEC5083E07CE303EB2C227636F3B0E69E45F866BCBCEED86318ECF8F3549C70C8DC88EC01D9722EFC2E7B1B295C85CE0A2BC0E30BCC6524B1911DFEE2008357E11A4C29F27C42831635581BD326FAE2AB9FEC74DE31A3B24DDBBC88E5AB175864FD51198762AE146D3286556F3F48D51F3B7F0153BCC6B7EB6D7B5A8F10B9134628CD3C6BE979DC26FAA476536DEB0B698E7A6F0A0CE2C8AFE58CC1AFBF821234E5D21F9B47B023257C14DD78FE096DFF136165BF9C2BCD5125A2393A3971592CAAEB0DC2A36E7EC40EF057080E5A29C48E4CCE2ACF786042AD4005433491CCC7D55A1F15575AB41D530C1F7FD19F28475C9C9A4548FE7C3E4298D460D882648C9A5F07172482123C39907BD9A885F16D29EACCFD03D27F87E9563E99A6C2C7E798E603561E97AE3CDBB185A7970E655C6016908654B7FCC8EDF36A5E2AC94ACBD29BD2A83C20C87C19CADB29BD5F61690A845FB6EB947DA23FECFFDD4F9139492EE149614DB54850E02374EA602B42C726A65DFDA81C54B2E027880B49CCE2D16607AA87C08EE0986FED8540FAF2761C44C208DA20D659C86777FD26498A3CACBC1C4270BAF96A001072AA7F7AEC171D1D3E514F27D957B885EF217A32C65565D765794A6CE877D442CBFA4562554C6CA73A4510A401BFFFD4923AA560C414750FDAD7420DEBEBF232B8E26A50308E29B8A238724B2D14AAA156E4145EB3A151A145A3012102CFC8CA4B46C54B2652F1D29CEA9F905CE25DF61012DD58ADE9EA3B6ED24E713229222EB39FA58DD73A4B7674304AB8B2784B6F627826F530C6B1F381A634E0FC0560BAAAA10275B8A0936E0CC385B1377764459D5695DA7DBB061574363AA79D8EDC1B322D0879DF89D6E77ACD922F22E6CAD8340A581D5403E8840817CD0AA07CE8AD202FB76691C4813A8231BDEEEF75CAC34BA184CA6CDE69D3F142B18F31BA50471BA6EDA17A0BE6BFF5F45D74982F859639775110016E95D0FDBA72FE7F352D132AC80A8C926AF008D15022D4CC35268E721919B89E6AF590DDAA397692058787D721B88E5D464876B867E84593A1F4F336606B026BC4DA7AFC7C985208BE09C4097D2315813C353A6E37C13A4CF459A97D78D90C882B1D3B29701560CFCE5B2EDE98D7B6BFD015115C4CF71F4FB3BD65282B3F46C349C2A214319C734C7EC3D8BCEB3F014228511F7CAB7F3BAAE56364BA0862FAFB5FD2976C6F922357B42D01899DE2CC26E9752BD0BAA6675BF07FF413835661C2BCF72F643AC14F7767FF21F9A37D2BF7B5765E18A4D58953D7C0EF90BD0E502E3D9A27951BCD476CD8D7EAA8A58604B2D70E49D26C7B3D91CDCDE527BE5552FF2641CA590E0C4DA0FEA2B674B8F968039C64829BD66BC74E3530A64865D75A23BFBE33E5894AA4BBE8E97EFD92BFE4C9C00179CC76CF13EB0998C444746AEC18306A301C936623E2030355E0D00D7A40B6DB574E23E577F49C5A4BB949B4F936FD2F9DFC1709D5293C2F9A215E96AF000E6288C2534CC988F976C4EDD1092424D017D03D7707A7E3A1763C16A08701124748819A36487DE86A46D5357AD35ED944C3EEA7C1E538614B11EC919DCCBB50A27382F0A61905F99FFAD819F7A97B57EA50E509991FEE6714B924B74722BABE7AEA483EFFC7E16C0791932EAB66A38D16F5408E08912E9A833A908AA9812ED16BE270EDBB0A704A7E66C133A3CB7ED0886A7B43FBA5939CB39B8D2AB469311F4249D7E7E946AFA7FB37DD52ED9373B21E7D7E674939670C95B54B"),
    "PageName": (None, "DefaultResult"),
    "DBCode": (None, "SCDB"),
    "KuaKuCodes": (None, "CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCVD,CJFN,CCJD"),
    "CurPage": (None, "1"),
    "RecordsCntPerPage": (None, "50"),
    "CurDisplayMode": (None, "listmode"),
    "CurrSortField": (None, "%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)"),
    "CurrSortFieldType": (None, "desc"),
    "IsSortSearch": (None, "false"),
    "IsSentenceSearch": (None, "false"),
    "Subject": (None, )
}

def GetFormData(
    author: str, school: str = "中国人民大学", curPage: int = 1, 
    details: bool = True
):
    formData = deepcopy(
        customModeFormDataTemplate if details 
        else listModeFormDataTemplate
    )
    formData["QueryJson"] = (
        formData["QueryJson"][0],
        (formData["QueryJson"][1]).\
            replace("这是作者的名字", author).\
                replace("中国人民大学", school)
    )
    formData["CurPage"] = (None, str(curPage))
    return formData

def GetHeaders() -> dict:
    return cnkiHeaders
