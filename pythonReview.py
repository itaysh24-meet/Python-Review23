def create_youtube_video(title, description):
	video = {"name": title, "description": description, "likes": 0, "dislike": 0, "commants": {"username": ""}}
	return video

def like(ytvideo):
	if "likes" in ytvideo:
		ytvideo["likes"] += 1

	return ytvideo

def dislike(ytvideo):
	if "dislike" in ytvideo:
		ytvideo["dislike"] += 1

	return ytvideo

def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video

video = create_youtube_video("My video", "this is my first video")

for i in range(495):
	like(video)

print(video)