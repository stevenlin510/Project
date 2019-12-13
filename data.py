import twint

c = twint.Config()
a = twint.Config()
b = twint.Config()

c.Search = "Amazon forest"
c.Lang = 'en'
c.Limit = 10000
c.Since = '2019-01-01'
c.Store_csv = True
c.Output = "Amazon forest"
c.Hide_output = True

twint.run.Search(c)

a.Search = "Amazon forest fire"
a.Lang = 'en'
a.Limit = 10000
a.Store_csv = True
a.Since = '2019-01-01'
a.Output = " Amazon forest fire"
a.Hide_output = True
twint.run.Search(a)

b.Search = "Amazon forest", ' fire',  "climate change"
b.Lang = 'en'
b.Limit = 10000
b.Since = '2019-01-01'
b.Store_csv = True
b.Output = " climate change"
b.Hide_output = True
twint.run.Search(b)

d= twint.Config()
d.Search = 'brazil amazon'
d.Limit = 10000
d.Lang = 'en'
d.Store_csv = True
d.Output = 'brazil amazon'
d.Since = '2019-01-01'
d.Hide_output = True
twint.run.Search(d)
