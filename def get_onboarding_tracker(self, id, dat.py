 def get_onboarding_tracker(self, id, data):
        client = pymongo.MongoClient()
        client.frogdata.authenticate(
            config.MONGO_FROGDATA_USERNAME,
            config.MONGO_FROGDATA_PASSWORD
        )
        db = client['frogdata']
        dealer_list = list(db.dealerinfo.find())
        records = []
        for each_dealer in dealer_list:
            if each_dealer["dealerName"].lower() != "system" and each_dealer["dealerName"].lower() != "demo" and each_dealer["dealerName"].lower() != "frogdata":
                data = {"dealer_name": each_dealer["dealerName"]}
                data["group_name"] = each_dealer.get("group_name")
                data["dealer_short_name"] = each_dealer.get("dealerShortName")
                data["dms_data_source"] = each_dealer.get("dataProviders").get("dms").get("name")
                data["crm_data_source"] = each_dealer.get("dataProviders").get("crm").get("name")
                data["web_data_source"] = each_dealer.get("dataProviders").get("web").get("name")
                data["pricing_data_source"] = each_dealer.get("dataProviders").get("pricing").get("name")
                data["vehicle_appraisal_data_source"] = each_dealer.get("dataProviders").get("appraisal").get("name")
                data["tread_wear_data_source"] = each_dealer.get("dataProviders").get("tire").get("name")
                data["sign_up_date"] = each_dealer.get("signupDate")
                data["owner"] = each_dealer.get("setupBy")
                data["dealer_id_cdk"] = each_dealer.get("cdk_dealer_id")
                data["inventory_company_cdk"] = each_dealer.get("cdk_inventory_company")
                data["company_number_cdk"] = each_dealer.get("cdk_company_number")
                data["enterprise_code_ot"] = each_dealer.get("ota_enterprise_code")
                data["ota_company_number_ot"] = each_dealer.get("ota_company_number")
                data["acct_company_number_ot"] = each_dealer.get("accounting_company_number")
                records.append(data)
        html_dump = pandas.DataFrame(records)
        html_dump = html_dump.sort_values(by=["dealer_name"]).reset_index(drop=True)
        html_dump = html_dump[["group_name","dealer_name","dealer_short_name","dms_data_source","crm_data_source","web_data_source","pricing_data_source","vehicle_appraisal_data_source","tread_wear_data_source","sign_up_date","owner","dealer_id_cdk","inventory_company_cdk","company_number_cdk","enterprise_code_ot","ota_company_number_ot","acct_company_number_ot"]]
        html_dump.to_csv("/home/ubuntu/piyush-test/html_dump.csv")
        return True, {"status": "ok", "html_dump": list(html_dump.T.to_dict().values())}
        """"