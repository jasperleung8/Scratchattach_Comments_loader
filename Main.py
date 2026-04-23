import scratchattach as sa

session = sa.login_by_id("Your session id here", username="jasperbro") 

cloud = session.connect_cloud("your project id here")

client = cloud.requests()

client.send("server started")
@client.request
def ping(): 
    print("Ping request received")
    return "pong"

@client.request
def Comments(argument1):
    project = session.connect_project(argument1)
    if project.comments_allowed :
        Comments = project.comments(limit=20, offset=0)
        return_comment = []
        for comment in Comments :
            author = comment.author
            content = comment.content
            time = comment.datetime_created
            return_comment.append(f"{comment.author()} : {comment.content} at {comment.datetime_created}")
            replies = comment.replies(limit=4)
            for reply in replies :
                return_comment.append(f"        {reply.author()} : {reply.content} at {reply.datetime_created}")
    else :    
        return_comment = "Not allowed"
    return return_comment

@client.request
def Update():
    project = session.connect_project("1212801905")
    Comments = project.comments(limit=20, offset=0)
    return_comment = []
    return_comment.append("Click green flag, wait and reload to see change !")
    for comment in Comments :
        author = comment.author
        content = comment.content
        time = comment.datetime_created
        return_comment.append(f"{comment.author()} : {comment.content}")
        replies = comment.replies(limit=20)
        for reply in replies :
            return_comment.append(f"        {reply.author()} : {reply.content}")
    projectset = session.connect_project("1212801905")
    set = "Comments for this project :"
    for item in return_comment :
        set = f"{set}\n{item}"
    projectset.set_notes(set)
    return "Updated"

client.start(thread=True)
