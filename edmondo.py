import webapp2

from google.appengine.ext import db

class Scores(db.Model):
  session = db.StringProperty(multiline=False) 
  name = db.StringProperty(multiline=False)
  score = db.IntegerProperty()
 
class MainPage(webapp2.RequestHandler):
  def get(self):

    session=self.request.get('session') #the session
    name=self.request.get('name') # name
    score=long("0"+self.request.get('score')) # score
 
    if self.request.get('type')=='add':  # Adding a new score
          q = db.GqlQuery("SELECT * FROM Scores WHERE session = :k1 AND name = :k2",k1=session, k2=name)
          count=q.count(2)
 
          if count==0 :  # the service doesn't exist, so add it.
              if session=="" or name=="" :
                  self.response.out.write('must provide session, name')
              else:
                  newrec=Scores(session=session,name=name,score=score)
                  newrec.put()
                  self.response.out.write('Added new score for ' + name)
          else:
              rec=q.get()
              rec.score = rec.score + score
              rec.put()
              self.response.out.write('Updated '+name+" now is "+str(rec.score))
    elif self.request.get('type')=='list':
        q = db.GqlQuery("SELECT * FROM Scores WHERE session = :k1 ORDER BY score DESC",k1=session)
        count = q.count(2)
        #self.response.out.write("Found "+str(count)+" results ")
        if count==0 :
              self.response.out.write('Empty') 
        else:
              results = q.fetch(1000)
              for result in results:
                 self.response.out.write(result.name+','+str(result.score)+"\n") 
              self.response.out.write('END')  # Cap the list

    elif self.request.get('type')=='clear':
          q = db.GqlQuery("SELECT * FROM Scores WHERE session = :kk",kk=session)
          count=q.count(2)
 
          if count==0 :
            self.response.out.write('None')
          else:
            results=q.fetch(100)
            db.delete(results)  
            self.response.out.write('Removed '+str(count))
         


app = webapp2.WSGIApplication([
	('/', MainPage),
	],
debug=True)