from mangum import Mangum

from index import app

handler = Mangum(app)
