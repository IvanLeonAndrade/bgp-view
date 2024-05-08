import requests

def get_asn_data(asn):
    url = f'https://api.bgpview.io/asn/{asn}/upstreams'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Devuelve el contenido JSON de la respuesta
    else:
        return f'Error: {response.status_code}'
    
def obtener_descripciones(desc):
    # vec = desc['description']
    vec = desc['name']
    return vec




while True:
    asn = input('Ingrese AS o [x] Para Salir ')
    if asn.lower() == 'x':
        exit()

    asn_data = get_asn_data(int(asn))

    if len(asn_data['data']['ipv4_upstreams']) == 0:
        print('ERROR: EL ASN NO EXISTE')
        continue
            
    proovedores_ipv4_upstreams = map(obtener_descripciones, asn_data['data']['ipv4_upstreams'])
    proovedores_ipv6_upstreams = map(obtener_descripciones, asn_data['data']['ipv6_upstreams'])

    i = 1
    print('\nProovedores - ipv4_upstreams:\n')
    for s in proovedores_ipv4_upstreams:
        print(f'{i}) ', s)
        i += 1
        
    print('\n')

    i = 1
    print('\nProovedores - ipv6_upstreams:\n')
    for s in proovedores_ipv6_upstreams:
        print(f'{i}) ', s)
        i += 1



