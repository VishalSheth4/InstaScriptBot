# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'life_explorer_4'
insta_password = 'tigerF1sh00'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username="life_explorer_4",
                  password="tigerF1sh00",
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """	
  #follow
  # session.follow_user_followers('disha_patel143',
  #                                 amount=500,
  #                                 randomize=True, sleep_delay=600,
  #                                 interact=True)
	
  # general settings		
  # session.set_dont_include(["disha_patel143", "becometraveller_", "Jay_modi_21"])		
  
  # activity		
  session.like_by_tags(["natgeo","travel"], amount=100000)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=85)
  session.set_comments(comments)
  session.join_pods(topic='sports', engagement_mode='no_comments')
