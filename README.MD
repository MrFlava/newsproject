Steps to run on localhost:

    1. Clone the project using git clone
    2. Install all requirement modules using pip 
    3. In the main directory  (newsproject) create local_settings.py with SECRET_KEY and database data
    4. Create build using docker-compose build
    5. Run the container using docker-compose up

After that, you can use Postman for testing this API.
Here's list of variables and methods for requests:

    1. base_url http://127.0.0.1:8000/ 
    2. register_url auth/users/ - POST - user registration
    3. login_url auth/token/login - POST - user login
    4. logout_url auth/token/logout - POST - user logout
    5. posts_url api/news/show-posts - GET - get all posts
    6. create_posts_url api/news/create-post - POST - GET - create own post
    7. update_post_url api/news/update-post - PATCH - update own post
    8. delete_post_url api/news/delete-post - DELETE - delete own post
    9. create_comment_url api/news/create-comment - POST - create comment under the post
    10. show_comment_url api/news/show-comments - GET - show  all comments 
    11. upvote_post_url api/news/upvote-post - POST  - upvote for the post


    


