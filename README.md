Simple Rest application to scrape title data from given urls

This is rest based web crawler, when any url is given, it returns it's title and url itself.

So after downloading the project, run the server and open 'http://127.0.0.1:8000/url-create/' and post list of urls with django rest framowork default theme or with Postman. Like,

["https://www.youtube.com/watch?v=RBumgq5yVrA&list=RDRBumgq5yVrA&start_radio=1", "https://www.youtube.com/watch?v=450p7goxZqg&list=RDRBumgq5yVrA&index=3", "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=RDRBumgq5yVrA&index=4"]

and then program returns to

[ { "url": "https://www.youtube.com/watch?v=RBumgq5yVrA&list=RDRBumgq5yVrA&start_radio=1", "title": "Passenger | Let Her Go (Official Video) - YouTube" }, { "url": "https://www.youtube.com/watch?v=450p7goxZqg&list=RDRBumgq5yVrA&index=3", "title": "John Legend - All of Me (Official Video) - YouTube" }, { "url": "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=RDRBumgq5yVrA&index=4", "title": "Ed Sheeran - Perfect (Official Music Video) - YouTube" } ]

This is backend of the project. Frontend is being written in VueJs as you can check in frontend folder but not ready yet.
