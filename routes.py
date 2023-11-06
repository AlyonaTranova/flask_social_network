from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
	return render_template('/index.html')


def add_tweet():
	pass


def delete_tweet():
	pass


def follow_user():
	pass


def unfollow_user():
	pass


def like_tweet():
	pass


def delete_like_tweet():
	pass


def get_all_tweets():
	pass


if __name__ == "__main__":
	app.run()
