from admitad import api, items

client_id = "3h7CgNIiNS38GjteF8yKOsoFKvTBpy"
client_secret = "yZ7AgTRwtCPI7GLmT0y5dOeJ1J0GqI"
scope = 'deeplink_generator websites advcampaigns'


client = api.get_oauth_client_client(
    client_id,
    client_secret,
    scope
)

def lamoda_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 1001, ulp=url, subid='AS32djkd31')
    return res[0]

def superstep_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 13978, ulp=url, subid='AS32djkd31')
    return res[0]

def brandshop_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 24411, ulp=url, subid='AS32djkd31')
    return res[0]

def shopotam_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 26887, ulp=url, subid='AS32djkd31')
    return res[0]

def urbanvibes_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 25929, ulp=url, subid='AS32djkd31')
    return res[0]

def elyts_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 14482, ulp=url, subid='watch')
    return res[0]

def bestwatch_admitad(url: str):   
    res = client.DeeplinksManage.create(2610012, 1950, ulp=url, subid='watch')
    return res[0]