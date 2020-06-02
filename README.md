`strl` keeps list like data at disk storage insted of memory.

## Benefits

By using disk storage, there is following advantages.

- reduce memory usage
- store the data after exit
- view and edit data by text editor
- easy to handle compared to sql

By this package, you can store the data like list, and the data will be stored in files in "__strl__" folder. You can reduce memory usage by saving at storage file. Especially in cloud servers, the cost increases in accordance with memory amount. In order to save cost, reduce memory usage is key factor.
In addition, this package is convenient as simple storage substitute for sql. Sometimes you just want to save single piece of data, sometimes sql is cumbersome for study or test.


## Sample usage1(create file)

```python
import strl

#
# create file
#

#mode w creates "people" file in "__stlist__" folder. if file exist, rewrite the file.
ppl = strl.STRL("people",mode="w")

#
# add data
#

ppl.append({"name":"bob","age":21})

people = [
  {"name":"tom","age":51},
  {"name":"linda","age":19},
  ]

ppl.append_list_items(people)


#
# return data
#

for item in ppl:
  print(item["name"]) #bob,tom,linda

print(ppl.get_item(1)) #{'name': 'tom', 'age': 51}
print(ppl.get_list()) # [{'name': 'bob', 'age': 21}, {'name': 'tom', 'age': 51}, {'name': 'linda', 'age': 19}]

filtered = ppl.get_filtered_list(lambda x: True if x["age"] <= 30 else False)
print(filtered) # [{'name': 'bob', 'age': 21}, {'name': 'linda', 'age': 19}]

#
# edit data
#

ppl.set(1, {"name":"john","age":45})
print(ppl.get_list()) #[{'name': 'bob', 'age': 21}, {'name': 'john', 'age': 45}, {'name': 'linda', 'age': 19}]

#give tuple to remove
ppl.remove((0,2))
print(ppl.get_list()) ##[{'name': 'john', 'age': 45}]

ppl.insert(1, {"name":"mike","age":30})
print(ppl.get_list()) #[{'name': 'john', 'age': 45}, {'name': 'mike', 'age': 30}]

```

## Sample usage2(load file)


```python
import strl

print(strl.STRL.show_files())  #['test', 'people', 'test2']

#mode l load the file. if not exist, create file.
#before loading, please change directory to the parent folder of "__stlist__" folder
ppl = strl.STRL("people",mode="l")

#when you created the data as Sample usage1
print(ppl.get_list()) #[{'name': 'john', 'age': 45}, {'name': 'mike', 'age': 30}, {'name': 'nana', 'age': 49}]

ppl.delete()

print(strl.STRL.show_files()) #['test', 'test2']

```

