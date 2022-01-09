from website.modules.supabase import SupaBase




def is_in_database(wallet_address):
    database = SupaBase()
    db = database.read_table('User_Data')
    for i in db:
        if i['wallet_address'] == wallet_address:
            return True
    
    return False