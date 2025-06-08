def verificaExisteManifestante(email, manifestantes):
    idUsuario = None
    existe = False

    ids = [manifestante['id'] for manifestante in manifestantes]
    
    if (ids):
        ids.sort()
        idProxUsuario = ids[-1]+1
    else:
        idProxUsuario = 1

    emails = [manifestante['email'] for manifestante in manifestantes]

    for idEmail in range(len(emails)):
        if(emails[idEmail] == email):
            existe = True
            idUsuario = idEmail+1
    
    if(existe):
        return existe, idUsuario
    else:
        return existe, idProxUsuario
