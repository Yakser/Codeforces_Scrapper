import requests
import json
import tkinter

main_url = "https://codeforces.com/api/"
methodName = "user.info?handles="


def get_info(event):
    username = entry_handle.get()

    r = requests.get(main_url + methodName + username)
    r = json.loads(r.text)

    if r['status'] == 'FAILED':
        lbl_handle.config(text="User not found.", font='Arial 15', fg='#e8793e', bg='#b1cbe0')

        lbl_rating.config(text="Rating: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        lbl_rank.config(text="Rank: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        lbl_maxRating.config(text="Max rating: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        lbl_maxRank.config(text="Max rank: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        return
    req = r['result'][0]

    lbl_handle.config(text=req['handle'], font='Arial 15', fg='#e8793e', bg='#b1cbe0')  # handle

    if 'rating' not in req:
        lbl_rating.config(text="Rating: -", font='Arial 12',
                          fg='#4e70ba', bg='#b1cbe0')

        lbl_rank.config(text="Rank: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        lbl_maxRating.config(text="Max rating: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        lbl_maxRank.config(text="Max rank: -", font='Arial 12', fg='#4e70ba', bg='#b1cbe0')

        return

    lbl_rating.config(text="Rating: " + str(req['rating']), font='Arial 12',
                      fg='#4e70ba', bg='#b1cbe0')  # rating

    lbl_rank.config(text="Rank: " + req['rank'].capitalize(), font='Arial 12',
                    fg='#4e70ba', bg='#b1cbe0')  # rank

    lbl_maxRating.config(text="Max rating: " + str(req['maxRating']), font='Arial 12',
                         fg='#4e70ba', bg='#b1cbe0')  # max rating

    lbl_maxRank.config(text="Max rank: " + req['maxRank'].capitalize(), font='Arial 12',
                       fg='#4e70ba', bg='#b1cbe0')  # max rank


master = tkinter.Tk()
master.title("CF_Scrapper")
master.geometry("250x250")
master.resizable(0, 0)

master.config(bg='#b1cbe0')
master.bind("<Return>", get_info)

lbl_username = tkinter.Label(text='Username(handle):', font='System 10', fg='#4e70ba', bg='#b1cbe0')
lbl_username.grid(row=0, column=0, padx=5, pady=5)

lbl_handle = tkinter.Label(text="Enter username", font='Arial 15',
                           fg='#e8793e', bg='#b1cbe0')
lbl_rating = tkinter.Label(text="Rating: -", font='Arial 12',
                           fg='#4e70ba', bg='#b1cbe0')
lbl_rank = tkinter.Label(text="Rank: -", font='Arial 12',
                         fg='#4e70ba', bg='#b1cbe0')
lbl_maxRating = tkinter.Label(text="Max rating: -", font='Arial 12',
                              fg='#4e70ba', bg='#b1cbe0')
lbl_maxRank = tkinter.Label(text="Max rank: -", font='Arial 12',
                            fg='#4e70ba', bg='#b1cbe0')

lbl_handle.grid(column=0, row=3, pady=5, columnspan=2)
lbl_rating.grid(column=0, row=4, pady=5, columnspan=2)
lbl_rank.grid(column=0, row=5, pady=5, columnspan=2)
lbl_maxRating.grid(column=0, row=6, pady=5, columnspan=2)
lbl_maxRank.grid(column=0, row=7, pady=5, columnspan=2)

entry_handle = tkinter.Entry(width=12, bg='#e8793e', fg='#b1cbe0', font='System 10', relief='flat')
entry_handle.grid(row=0, column=1, padx=5, pady=5, sticky="NW")

master.mainloop()
