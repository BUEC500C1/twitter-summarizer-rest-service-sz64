from requests import get, put
import time;

testput = put('http://18.188.22.159:80/Google').json();
print(testput);

time.sleep(15);

response = get('http://18.188.22.159:80/Google');
test = open('test.mp4', 'wb');
test.write(response.content);