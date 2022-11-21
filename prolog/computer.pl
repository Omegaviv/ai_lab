suggest(S):-
write("What are you interested in ? "),
read(I),
write("What is your preferred Language ?"),
read(L),
write('What is your age ?'),
read(A),
book(S,I,L,A).

book('b1',I,L,A):- 
(I= (history);I=(motivation)),
L=marathi,
A >=18,
!.
book('b2',I,L,A):- 
(I= (autobiography);I=(motivation)),
L=marathi,
A < 18,
!.

book('b3',I,L,A):- 
(I= (history);I=(autobiography)),
L=english,
A >=18,
!.

book('b4',I,L,A):- 
(I= (history)),
L=english,
A < 18,
!.

