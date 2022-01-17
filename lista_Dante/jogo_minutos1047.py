def hora (h_inicial,h_final):
    hora_calcualda = h_final - h_inicial
    return hora_calcualda

def minuto (m_inicial,m_final):
    minuto_calculado = m_final - m_inicial
    return minuto_calculado


h_inicial, m_inicial,h_final,m_final = map(int, input().split())

hora_total = hora(h_inicial,h_final)
minuto_total = minuto(m_inicial,m_final)

if hora_total == 0 and minuto_total == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

elif hora_total == 1 and minuto_total < 0:
    print('O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)')

elif hora_total == 0 and minuto_total >= 1:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora_total,minuto_total))

else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora_total,minuto_total))