girls = ['jane', 'ashley', 'mary','dd']
boys = ['justin', 'eric', 'david', 'she']
pair = list(map(list,zip(girls, boys)))

print(pair) #[('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]