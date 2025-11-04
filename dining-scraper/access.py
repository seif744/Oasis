from supabase import create_client
import pandas as pd
from datetime import datetime


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)


#supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

today = datetime.now().strftime('%Y-%m-%d')

print(f"Fetching menu for: {today}")

#response = supabase.table('menu_items').select('*') .eq('date', today).execute()

#df = pd.DataFrame(response.data)
#print(df)
#df.to_csv('menu.csv', index=False)
