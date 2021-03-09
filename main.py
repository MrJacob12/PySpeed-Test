import speedtest   
import json

st = speedtest.Speedtest()  

ab = st.download()
a = ((ab / 8) / 1024) / 1024 
print("Download:",a,"MB")  

ba = st.upload()
b = ((ba / 8) / 1024) / 1024  
print("Upload:",b,"MB")

servernames = []   
st.get_servers(servernames)   
print("Ping: ",st.results.ping,"ms")   

data = {}
data['download'] = []
data['download'].append({
    'MB': a,
    'b': ab
})
data['upload'] = []
data['upload'].append({
    'MB': b,
    'b': ba
})

with open('data.json','w') as outfile:
    json.dump(data, outfile)