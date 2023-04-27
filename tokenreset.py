from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('A@Bullela@_3',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
