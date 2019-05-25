from handlers.commentitemhandler import CommentItemHandler
from handlers.mainpagehandler 	 import MainPageHandler
from handlers.postinfohandler 	 import PostInfoHandler
from handlers.searchpagehandler  import SearchPageHandler
from handlers.singleitemhandler  import SingleItemHandler
from handlers.typeshandler 		 import TypesHandler
from handlers.rankpagehandler 	 import RankPageHandler
from handlers.loginhandler 	 import LoginHandler
from handlers.logouthandler import LogoutHandler
from handlers.signhandler import SignHandler
from handlers.subscripHandler import SubscriptionPageHandler
from handlers.myposthandler import MypostPageHandler
from handlers.reporthandler import ReportHandler

urls=[		
		(r'/',MainPageHandler),
		(r'/po', PostInfoHandler),
        (r'/item',SingleItemHandler),
        (r'/search',SearchPageHandler),
        (r'/comment',CommentItemHandler),
        (r'/types',TypesHandler),
        (r'/rank',RankPageHandler),
        (r'/login',LoginHandler),
        (r'/logout',LogoutHandler),
        (r'/signin',SignHandler),
        (r'/subscription',SubscriptionPageHandler),
        (r'/mypo',MypostPageHandler),
        (r'/report',ReportHandler)
]
