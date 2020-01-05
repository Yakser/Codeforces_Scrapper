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
        lbl_handle.config(text="User not found.")
        # clear
        lbl_rating.config(text="Rating: -")
        lbl_rating.pack()

        lbl_rank.config(text="Rank: -")
        lbl_rank.pack()

        lbl_maxRating.config(text="Max rating: -")
        lbl_maxRating.pack()

        lbl_maxRank.config(text="Max rank: -")
        lbl_maxRank.pack()
        #
        return
    req = r['result'][0]

    lbl_handle.config(text=req['handle'])  # handle
    lbl_handle.pack()

    if 'rating' not in req:
        lbl_rating.config(text="You didn't participate in official competitions")
        lbl_rating.pack()
        # clear
        lbl_rank.config(text="Rank: -")
        lbl_rank.pack()

        lbl_maxRating.config(text="Max rating: -")
        lbl_maxRating.pack()

        lbl_maxRank.config(text="Max rank: -")
        lbl_maxRank.pack()
        #
        return

    lbl_rating.config(text="Rating: " + str(req['rating']))  # rating
    lbl_rating.pack()

    lbl_rank.config(text="Rank: " + req['rank'].capitalize())  # rank
    lbl_rank.pack()

    lbl_maxRating.config(text="Max rating: " + str(req['maxRating']))  # max rating
    lbl_maxRating.pack()

    lbl_maxRank.config(text="Max rank: " + req['maxRank'].capitalize())  # max rank
    lbl_maxRank.pack()


master = tkinter.Tk()
master.geometry("250x250")
master.bind("<Return>", get_info)

lbl_handle = tkinter.Label(text='')
lbl_rating = tkinter.Label(text='')
lbl_rank = tkinter.Label(text='')
lbl_maxRating = tkinter.Label(text='')
lbl_maxRank = tkinter.Label(text='')

entry_handle = tkinter.Entry(width=30)
entry_handle.pack()

master.mainloop()
