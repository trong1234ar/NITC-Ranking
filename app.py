import streamlit as st
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
from config import *

st.set_page_config(
    page_title="NITC Ranking",
    page_icon="https://scontent.fhan5-2.fna.fbcdn.net/v/t39.30808-6/418864531_754000653441812_2333852474863752453_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9c7eae&_nc_ohc=f2RueeH4bg4AX9LlwWE&_nc_ht=scontent.fhan5-2.fna&oh=00_AfBTGjsoUsyXneQ9pA8Vi_4V2oVi9HCactgYg1fFreTyNw&oe=65C5BA53", 
    layout="wide",
)

back_ground_color()
local_css('style.css')

st.markdown(css_box_normal, unsafe_allow_html=True)
st.markdown(css_box_top, unsafe_allow_html=True)

side_col, main_col, tmp_col = st.columns([1, 3, 1])
with main_col:
    gsheetkey = "1vDWzUhdwYFSlHD-lbwisliJaON0bTT8fsUgZW3EwBno"

    url = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
    df = pd.read_excel(url)

    async def fetch_data(session, username):
        spoj_url = f'https://www.spoj.com/PTIT/users/{username}/'
        async with session.get(spoj_url) as response:
            return await response.text()

    async def process_user(session, i, df_row, results):
        NAME, USERNAME = df_row['Họ và tên'], df_row['Tên username']
        spoj_html = await fetch_data(session, USERNAME)
        html = BeautifulSoup(spoj_html, 'html.parser')
        tables = html.find_all('table', class_='table table-condensed')

        da_acc = tables[0].find_all('td')
        da_acc_list = [x.text for x in da_acc if x.text]

        chua_acc_list = []
        if len(tables) >= 2:
            chua_acc = tables[1].find_all('td')
            chua_acc_list = [x.text for x in chua_acc if x.text]

        results.append([NAME, len(da_acc_list), len(chua_acc_list)])

    async def main():
        results = []
        async with aiohttp.ClientSession() as session:
            tasks = [process_user(session, i, df_row, results) for i, df_row in df.iterrows()]
            await asyncio.gather(*tasks)
        main_df = pd.DataFrame(results, columns=['Name', 'Acc', 'NotAcc'])
        main_df = main_df.sort_values(by='Acc', ascending=0)
        # for user in range(len(main_df)):
        #     name = main_df.iloc[user, 0]
        #     acc = main_df.iloc[user, 1]
        #     notAcc = main_df.iloc[user, 2]
        #     if user == 0:
        #         st.markdown(f"<div class='top-box'>{user + 1} {name} {acc} {notAcc} </div>", unsafe_allow_html=True)
        #     else:
        #         st.markdown(f"<div class='normal-box'>{user + 1} {name} {acc} {notAcc} </div>", unsafe_allow_html=True)
        for user in range(len(main_df)):
            name = main_df.iloc[user, 0]
            acc = main_df.iloc[user, 1]
            notAcc = main_df.iloc[user, 2]

            if user == 0:
                st.markdown(f"<div class='top-box'><div class='left-content'>{user + 1} {name} 🏆 </div><div class='right-content'><div class='acc'>{acc}</div><div class='notAcc'>{notAcc}</div></div></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='normal-box'><div class='left-content'>{user + 1} {name}</div><div class='right-content'><div class='acc'>{acc}</div><div class='notAcc'>{notAcc}</div></div></div>", unsafe_allow_html=True)
            st.write('')

    if __name__ == "__main__":
        asyncio.run(main())

with side_col:
    url =  "https://scontent.fhan5-2.fna.fbcdn.net/v/t39.30808-6/418864531_754000653441812_2333852474863752453_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9c7eae&_nc_ohc=f2RueeH4bg4AX9LlwWE&_nc_ht=scontent.fhan5-2.fna&oh=00_AfBTGjsoUsyXneQ9pA8Vi_4V2oVi9HCactgYg1fFreTyNw&oe=65C5BA53"
    st.image(url)



