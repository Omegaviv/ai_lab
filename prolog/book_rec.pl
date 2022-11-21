
suggest(S) :- 
write('What are you interested in?: '),
read(P),
            write('How is your prefered language?: '),read(M), 
            write('What is your Age?: '),read(X),
            write('*Note: if there is no match with your preferences then false is printed*'),
            book(S,M,X,P).

%marathi
book('chava',M,X,P):- M = marathi,X >= 18,(P= (history) ; P=(autobiography)),!.
book('Man Me he Vishwas: Vishwas Nagre Patil',M,X,P):- M = marathi ,(X =< 18 ; X >= 18),(P= (autobiography) ; P=(motivation)),!.

%english
book('Brief Answers to Big Questions',M,X,P):- M = english ,(X =< 18 ; X >= 18), (P= (science) ; P=(spaceResearch)),!.
book('Rich Dad Poor Dad',M,X,P):- M = english ,(X >= 18), (P= (finance) ; P=(motivation)),!.
book('You Can Win',M,X,P):- M = english ,(X =< 18 ; X >= 18), (P= (motivation) ; P=(inspiration) ; P=(selfHelp)),!.


%! is called cut and is used to reduce backtracking