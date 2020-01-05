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
        print("User not found.")
        return
    req = r['result'][0]
    print(req['handle'])  # handle
    if 'rating' not in req:
        print("You didn't participate in official competitions")
        return
    print(req['rating'])  # rating
    print(req['rank'].capitalize())  # rank
    print(req['maxRating'])  # max rating
    print(req['maxRank'].capitalize())  # max rank


master = tkinter.Tk()
master.geometry("250x250")
master.bind("<Return>", get_info)


entry_handle = tkinter.Entry(width=30)
entry_handle.pack()

master.mainloop()
