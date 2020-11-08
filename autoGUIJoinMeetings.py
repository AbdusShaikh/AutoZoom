import os, webbrowser, pyautogui as gui, time, datetime
from plyer import notification


def join_meeting(meeting_access, meeting_password):
    """Launches a meeting based on meeting_id and meeting_password
    """
    # converts url to meeting id if it is a url
    meeting_access = change_meeting_url(meeting_access)
    # opens zoom from the system
    os.system("open /Applications/zoom.us.app")
    time.sleep(3)
    # uses keyboard shortcut to select join
    gui.keyDown('command')
    gui.press('j')
    gui.keyUp('command')
    # meeting id textbox is active by default
    # so the meeting ID can be put in directly
    gui.write(str(meeting_access))
    # enter button proceeds to password page
    gui.press('enter', interval=2)
    # next screen has meeting password as default
    # so we can enter the password directly
    gui.write(str(meeting_password))
    # enter button proceeds to audio selection page
    gui.press('enter')


def change_meeting_url(meeting_url):
    """Strips the meeting url and keeps meeting id
    """
    meeting_id_len = 0
    for index in range(len(meeting_url)):
        if isInt(meeting_url[index]):
            meeting_id_len += 1
        else:
            meeting_id_len = 0
        if meeting_id_len == 10:
            if (index != len(meeting_url) - 1) and isInt(meeting_url[index + 1]):
                return meeting_url[index - 9:index + 2]
            return meeting_url[index - 9:index + 1]


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


#join_meeting("https://utoronto.zoom.us/j/3202461821",2343243)


def new_notification(meeting, message):
    notification.notify(
        title=meeting['name'],
        message=message,
        app_icon="C:/Users/Abdus Samad/Documents/Newhacks 2020/Zoom-icon.ico",
        timeout=30
    )


def parse_time(timedata):
    time = str.split(timedata[-5:], ':')
    return datetime.time(int(time[0]), int(time[1]))


#meetings = [{'name': 'calculus', 'start time': datetime.time(9, 0), 'days': ['monday', 'wednesday', 'friday'],
#             'link': 'https://utoronto.zoom.us/j/3202461821', 'password': 2343243}]

data = [{'name': 'MAT186', 'start time': datetime.time(1, 44), 'day': 'monday', 'link': 88263501559, 'password': 'pVp6aH'}]

meetings = [{'name': data[i]['name'], 'start time': data[i]['start time'], 'day': data[i]['day'],
            'link': data[i]['link'], 'password': data[i]['password']} for i in range(0, len(data))]

"""
while True:
    for meeting in meetings:
        if (str.lower(str.split(time.ctime())[0])) in meeting['day'] and \
                meeting['start time'].hour == time.localtime().tm_hour:
            if meeting['start time'].minute == (time.localtime().tm_min - 15):
                message = (meeting['name'], 'starts in 15 minutes')
                new_notification(meeting, message)
            elif meeting['start time'].minute == (time.localtime().tm_min - 5):
                message = (meeting['name'], 'starts in 5 minutes')
                new_notification(meeting, message)
            elif meeting['start time'].minute == time.localtime().tm_min:
                message = (meeting['name'], 'starts now!')
                new_notification(meeting, message)
                join_meeting(meeting['link'], meeting['password'])

"""

join_meeting("85465799479",'Ys6F2n')