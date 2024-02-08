from newsapp.models import *
u1=User.objects.create_user('Vasya')
u2=User.objects.create_user('Petya')
a1 = Author.objects.create(authorUser = u1)
a2 = Author.objects.create(authorUser = u2)
c1 = Category.objects.create(category = 'IT')
c2 = Category.objects.create(category = 'Politics')
c3 = Category.objects.create(category = 'Sport')
c4 = Category.objects.create(category = 'Nature')
post1 = Post.objects.create(postAuthor = a1, postType = 'AR', title = 'Post about sport', text = 'Какие-то слова и буквы. Много-много.')
post2 = Post.objects.create(postAuthor = a2, postType = 'AR', title = 'Post about politic', text = 'Какие-то слова и буквы. Много-много.')
post3 = Post.objects.create(postAuthor = a1, postType = 'NW', title = 'News about IT and Nature', text = 'Какие-то слова и буквы. Много-много.')
post1.categories.add(Category.objects.get(category = 'Sport'))
post2.categories.add(Category.objects.get(id = 2))
post3.categories.add(Category.objects.get(id = 1))
post3.categories.add(Category.objects.get(id = 4))
com1 = Comment.objects.create(post_comment = post1, comment_user = u2, comment_text = 'Какой-то коммент')
com2 = Comment.objects.create(post_comment = post2, comment_user = u1, comment_text = 'Какой-то гневный коммент')
com3 = Comment.objects.create(post_comment = post3, comment_user = u1, comment_text = 'Какой-то мем')
com4 = Comment.objects.create(post_comment = post1, comment_user = u1, comment_text = 'Какой-то позитив')
com1.like()
com1.like()
com1.like()
com1.like()
com2.like()
com2.dislike()
com2.dislike()
com3.dislike()
com3.like()
com4.dislike()
com4.like()
post1.like()
post1.like()
post1.like()
post1.dislike()
post2.like()
post2.dislike()
post2.like()
post2.dislike()
post3.like()
post3.like()
post3.like()
post3.dislike()
post3.like()
a1.update_rating()
a2.update_rating()
a = Author.objects.all().order_by('-rating_author')[:1]
a[0].authorUser.username
a[0].rating_author
p = Post.objects.all().order_by('-rating')
pt = p[0]
pt.time_in
pt.postAuthor.authorUser.username
pt.rating
pt.title
pt.preview()
co = Comment.objects.all().filter(post_comment = pt)
for i in co:
    i.time_in
    i.comment_user.username
    i.rating
    i.comment_text

