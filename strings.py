a="shyam"
b='shyam'
print(a)
print(a==b)


c='''Lorem ipsum dolor sit amet. Qui quas illo qui similique magnam ad galisum quisquam qui possimus exercitationem et corporis veniam ut sint quaerat non corporis nemo. Et nesciunt eius vel blanditiis enim et dolorem accusantium. Sed alias rerum non architecto eaque ad autem numquam hic possimus placeat ex maxime itaque aut assumenda odio est autem ducimus.
Ad voluptas cupiditate et galisum quibusdam eos officia delectus eum asperiores esse sed sunt nihil eos repudiandae laboriosam in galisum minus. Sed inventore magnam id eligendi fugit in possimus internos sit voluptatibus animi qui omnis enim eum aspernatur voluptas. Sit Quis aliquid eum architecto eveniet et corrupti placeat. Aut unde dignissimos qui obcaecati autem id sint aliquam et dolorem excepturi quo mollitia expedita aut officiis enim.

Non quod odio in voluptas voluptas et asperiores porro nam unde doloribus aut vitae voluptatum ut temporibus distinctio? Et neque voluptatum At recusandae excepturi et vero voluptas eos soluta repellendus. Ut sunt dolor et nihil velit sed ipsam voluptatem et aliquam illum'''

print(c)

print(a[0:3])

for x in a:
    print(x)

print(len(a))

# check value in string

txt = "The best things in life are free!"
print("free" not in txt)

if "free" in txt:
    print("heyy")

print(a[:3])

print(a.lower())


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, Horld!"
print(a.replace("H", "J"))

a="shyam@gmail.com"
username=a.split("@")[0]
domain=a.split("@")[1]

print(username,domain)