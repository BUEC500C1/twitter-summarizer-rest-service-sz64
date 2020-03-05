from requests import get, put
import time;

testput = put('http://localhost:5000/Google').json();
print(testput);

time.sleep(15);

response = get('http://localhost:5000/Google');
test = open('test.mp4', 'wb');
test.write(response.content);