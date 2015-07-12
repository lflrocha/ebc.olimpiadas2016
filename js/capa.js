function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

grandes = new Array(24)
grandes[0]  = ['BELO HORIZONTE','BHZ','001','0018','Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga']
grandes[1]  = ['BELO HORIZONTE','BHZ','001','0027','Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga']
grandes[2]  = ['BRASÍLIA','BSB','003','0002','Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga']
grandes[3]  = ['BRASÍLIA','BSB','007','0006','Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga']
grandes[4]  = ['CUIABÁ','CBA','001','0003','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
grandes[5]  = ['CUIABÁ','CBA','003','0001','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
grandes[6]  = ['CURITIBA','CUR','001','0002','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
grandes[7]  = ['CURITIBA','CUR','004','0002','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
grandes[8]  = ['FORTALEZA','FTL','005','0004','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
grandes[9]  = ['FORTALEZA','FTL','006','0004','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
grandes[10]  = ['MANAUS','MAN','002','0001','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
grandes[11]  = ['MANAUS','MAN','002','0024','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
grandes[12]  = ['NATAL','NTL','004','0014','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
grandes[13]  = ['NATAL','NTL','006','0004','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
grandes[14]  = ['PORTO ALEGRE','PTA','002','0007','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
grandes[15]  = ['PORTO ALEGRE','PTA','006','0002','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
grandes[16]  = ['RECIFE','RCF','002','0006','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
grandes[17]  = ['RECIFE','RCF','006','0001','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
grandes[18]  = ['RIO DE JANEIRO','RIO','002','0020','Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
grandes[19]  = ['RIO DE JANEIRO','RIO','005','0001','Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
grandes[20]  = ['SALVADOR','SAL','001','0002','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
grandes[21]  = ['SALVADOR','SAL','017','0002','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
grandes[22]  = ['SÃO PAULO','SAO','004','0009','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
grandes[23]  = ['SÃO PAULO','SAO','005','0006','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']


pequenas = new Array(48)
pequenas[0]  = ['BELO HORIZONTE','BHZ','003','0011','Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga']
pequenas[1]  = ['BELO HORIZONTE','BHZ','003','0016','Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga']
pequenas[2]  = ['BELO HORIZONTE','BHZ','007','0004','Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga']
pequenas[3]  = ['BELO HORIZONTE','BHZ','009','0005','Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga']

pequenas[4]  = ['BRASÍLIA','BSB','003','0003','Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[5]  = ['BRASÍLIA','BSB','003','0012','Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[6]  = ['BRASÍLIA','BSB','005','0010','Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[7]  = ['BRASÍLIA','BSB','005','0011','Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga']

pequenas[8]  = ['CUIABÁ','CBA','004','0008','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[9]  = ['CUIABÁ','CBA','004','0020','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[10]  = ['CUIABÁ','CBA','004','0025','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[11]  = ['CUIABÁ','CBA','004','0035','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga']

pequenas[12]  = ['CURITIBA','CUR','005','0002','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[13]  = ['CURITIBA','CUR','006','0002','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[14]  = ['CURITIBA','CUR','008','0008','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[15]  = ['CURITIBA','CUR','010','0015','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']

pequenas[16]  = ['FORTALEZA','FTL','001','0001','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[17]  = ['FORTALEZA','FTL','004','0006','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[18]  = ['FORTALEZA','FTL','008','0001','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[19]  = ['FORTALEZA','FTL','010','0005','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']

pequenas[20]  = ['MANAUS','MAN','001','0014','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[21]  = ['MANAUS','MAN','003','0004','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[22]  = ['MANAUS','MAN','003','0018','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[23]  = ['MANAUS','MAN','007','0021','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']

pequenas[24]  = ['NATAL','NTL','001','0003','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[25]  = ['NATAL','NTL','001','0013','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[26]  = ['NATAL','NTL','005','0006','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[27]  = ['NATAL','NTL','006','0007','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']

pequenas[28]  = ['PORTO ALEGRE','PTA','002','0010','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[29]  = ['PORTO ALEGRE','PTA','009','0010','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[30]  = ['PORTO ALEGRE','PTA','012','0018','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']
pequenas[31]  = ['PORTO ALEGRE','PTA','012','0035','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga']

pequenas[32]  = ['RECIFE','RCF','005','0003','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[33]  = ['RECIFE','RCF','005','0005','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[34]  = ['RECIFE','RCF','008','0001','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']
pequenas[35]  = ['RECIFE','RCF','012','0006','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga']

pequenas[36]  = ['RIO DE JANEIRO','RIO','002','0017','Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
pequenas[37]  = ['RIO DE JANEIRO','RIO','002','0021','Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
pequenas[38]  = ['RIO DE JANEIRO','RIO','005','0023','Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
pequenas[39]  = ['RIO DE JANEIRO','RIO','008','0002','Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']

pequenas[40]  = ['SALVADOR','SAL','003','0004','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[41]  = ['SALVADOR','SAL','006','0002','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[42]  = ['SALVADOR','SAL','012','0006','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']
pequenas[43]  = ['SALVADOR','SAL','014','0010','Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga ']

pequenas[44]  = ['SÃO PAULO','SAO','005','0012','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
pequenas[45]  = ['SÃO PAULO','SAO','005','0016','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
pequenas[46]  = ['SÃO PAULO','SAO','009','0004','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']
pequenas[47]  = ['SÃO PAULO','SAO','011','0011','Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga ']



var numeros = new Array();
numeros = shuffleArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
cid1 = numeros[0];
cid2 = numeros[1];
cid3 = numeros[2];
cid4 = numeros[3];

R1 = Math.floor(Math.random()*2);
var fotoMaior = cid1 * 2 + R1;

R2 = Math.floor(Math.random()*4);
var fotoMenor1 = cid2 * 4 + R2;

R3 = Math.floor(Math.random()*4);
var fotoMenor2 = cid3 * 4 + R3;

R4 = Math.floor(Math.random()*4);
var fotoMenor3 = cid4 * 4 + R4;
