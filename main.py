from abc import ABC, abstractmethod
import numpy as np

global RANG_SP

def kriterij(x1, x2):
    return 80 - (x1**2 - 10*np.cos(2*np.pi*x1)) - (x2**2 - 10*np.cos(2*np.pi*x2))

def binarniUDecimalni (broj):
    return int(broj, 2)

class ApstraktnaIndiviua (ABC):
    def __init__(self, DuzinaHromozoma):
        #generisanje slucajnog binarnog niza(Hromozom) duzine DuzinaHromozoma
        self.DuzinaHromozoma = DuzinaHromozoma
        niz = []
        for i in range(DuzinaHromozoma):
            temp = np.random.randint(2)
            niz.append(temp)
        self.Hromozom = niz
        self.SetFitness(self.Evaluiraj())
        super(ApstraktnaIndiviua, self).__init__()

    def GetDuzinaHromozoma (self):
        return self.DuzinaHromozoma

    def SetDuzinaHromozoma (self, DuzinaHromozoma):
        if (isinstance(DuzinaHromozoma, int) and DuzinaHromozoma >= 4):
            self.DuzinaHromozoma = DuzinaHromozoma
        else:
            raise Exception ("Dužina hromozoma mora biti cijeli broj.")

    def GetHromozom (self):
        return self.Hromozom

    def SetHromozom (self, Hromozom):
        if (isinstance(Hromozom, list)):
            for broj in Hromozom:
                if broj != 0 and broj != 1:
                    raise Exception("Lista nije binarna.")
            self.Hromozom = Hromozom
        else:
            raise Exception("Hromozom treba biti niz(lista)")

    def GetFitness (self):
        return self.Fitness

    def SetFitness (self, Fitness):
        if (isinstance(Fitness, float)):
            self.Fitness = Fitness
        else:
            raise Exception("Fitness hromozoma mora biti tipa float.")

    def GetTacka(self):
        duzinaHromozoma = self.GetDuzinaHromozoma()
        hromozom = self.GetHromozom()
        predznakx1 = hromozom[0]  # prvi znak kada gledamo hromozom, ali posljednji po indeksaciji (d - 1)
        predznakx2 = hromozom[int((duzinaHromozoma // 2))]  # prvi znak nakon sredine, r - 1
        # print("Predznak x1 je ", predznakx1)
        # print("Predznak x2 je ", predznakx2)
        # racunanje x1
        #p = np.random.randint(1, int(duzinaHromozoma // 2) - 2)  # da tacke sigurno budu unutar problemskog prostora
        p = 2  #uzimamo 2 bita za cijeli dio
        cijeliDiox1 = []
        for i in range(1, 1 + p):
            cijeliDiox1.append(str(hromozom[i]))
        decimalniDiox1 = []
        for i in range(1 + p, int(duzinaHromozoma // 2)):
            decimalniDiox1.append(str(hromozom[i]))
        pom = ""
        # print("Cijeli dio x1 je ", cijeliDiox1)
        x1C = int(pom.join(cijeliDiox1), 2)
        # print("Deci dio x1 je ", decimalniDiox1)
        if len(decimalniDiox1) == 0:
            x1D = 0
        else:
            x1D = int(pom.join(decimalniDiox1), 2)
        x1 = float(str(x1C) + "." + str(x1D))
        if predznakx1 == 1 and x1C != 0 and x1D != 0:
            x1 *= (-1)
        # racunanje x2
        #p = np.random.randint(1, int(duzinaHromozoma // 2) - 2)
        p = 2
        cijeliDiox2 = []
        for i in range(int((duzinaHromozoma // 2) + 1), int((duzinaHromozoma // 2) + 1 + p)):
            cijeliDiox2.append(str(hromozom[i]))
        decimalniDiox2 = []
        for i in range(int((duzinaHromozoma // 2) + 1 + p), duzinaHromozoma):
            decimalniDiox2.append(str(hromozom[i]))
        # print("Cijeli dio x2 je ", cijeliDiox2)
        x2C = int(pom.join(cijeliDiox2), 2)
        # print("Dec dio x2 je ", decimalniDiox2)
        if len(decimalniDiox2) == 0:
            x2D = 0
        else:
            x2D = int(pom.join(decimalniDiox2), 2)
        x2 = float(str(x2C) + "." + str(x2D))
        if predznakx2 == 0 and x2C != 0 and x2D != 0:  # nema smisla da bude -0.0
            x2 *= (-1)
        return x1, x2

    @abstractmethod
    def Evaluiraj (self,):
        pass

class MojaIndividua (ApstraktnaIndiviua):
    def Evaluiraj(self):
        x1, x2 = self.GetTacka()
        fitness = 1*kriterij(x1, x2) + 0
        return fitness


class Populacija (object):
    def __init__(self, VelicinaPopulacije, VjerovatnocaUkrstanja, VjerovatnocaMutacije, MaxGeneracija, VelicinaElite, DuzinaHromozoma=16):
        #provjera ispravnosti parametara
        if (not isinstance(VelicinaPopulacije, int)):
            raise Exception("Veličina populacije mora biti cijeli broj.")
        if VjerovatnocaUkrstanja < 0 or VjerovatnocaUkrstanja > 1:
            raise Exception("Vjerovatnoća ukrštanja mora biti između 0 i 1.")
        if VjerovatnocaMutacije < 0 or VjerovatnocaMutacije > 1:
            raise Exception("Vjerovatnoća mutacije mora biti između 0 i 1.")
        if (not isinstance(MaxGeneracija, int)):
            raise Exception("Maksimalan broj generacija mora biti cijeli broj.")
        if (not isinstance(VelicinaElite, int) or VelicinaElite < 0 or VelicinaElite > 2):
            raise Exception("Veličina elite mora biti cijeli broj između 0 i 2.")
        if (DuzinaHromozoma < 4):
            raise Exception("Dužina hromozoma mora biti najmanje 4.")
        self.VelicinaPopulacije = VelicinaPopulacije
        self.VjerovatnocaUkrstanja = VjerovatnocaUkrstanja
        self.VjerovatnocaMutacije = VjerovatnocaMutacije
        self.MaxGeneracija = MaxGeneracija
        self.VelicinaElite = VelicinaElite
        self.DuzinaHromozoma = DuzinaHromozoma
        # generisanje jedne populacije
        self.Hromozomi = []
        for i in range(self.VelicinaPopulacije):
            self.Hromozomi.append(MojaIndividua(self.DuzinaHromozoma))

    def GetPopulacija(self):
        return self.Hromozomi

    def SetPopulacija(self, NoviHromozomi):
        self.Hromozomi = NoviHromozomi

    def SetVelicinaPopulacije (self, VelicinaPopulacije):
        if (isinstance(VelicinaPopulacije, int)):
            self.VelicinaPopulacije = VelicinaPopulacije
        else:
            raise Exception ("Veličina populacije mora biti cijeli broj.")

    def GetVelicinaPopulacije (self):
        return self.VelicinaPopulacije

    def SetVjerovatnocaUkrstanja(self, VjerovatnocaUkrstanja):
        if VjerovatnocaUkrstanja >= 0 and VjerovatnocaUkrstanja <= 1:
            self.VjerovatnocaUkrstanja = VjerovatnocaUkrstanja
        else:
            raise Exception ("Vjerovatnoća ukrštanja mora biti između 0 i 1.")

    def GetVjerovatnocaUkrstanja(self):
        return self.VjerovatnocaUkrstanja

    def SetVjerovatnocaMutacije(self, VjerovatnocaMutacije):
        if VjerovatnocaMutacije >= 0 and VjerovatnocaMutacije <= 1:
            self.VjerovatnocaMutacije = VjerovatnocaMutacije
        else:
            raise Exception ("Vjerovatnoća mutacije mora biti između 0 i 1.")

    def GetVjerovatnocaMutacije(self):
        return self.VjerovatnocaMutacije

    def SetMaxGeneracija(self, MaxGeneracija):
        if (isinstance(MaxGeneracija, int)):
            self.MaxGeneracija = MaxGeneracija
        else:
            raise Exception ("Maksimalan broj generacija mora biti cijeli broj.")

    def GetMaxGeneracija(self):
        return self.MaxGeneracija

    def SetVelicinaElite(self, VelicinaElite):
        if (isinstance(VelicinaElite, int) and VelicinaElite >= 0 and VelicinaElite <= 2):
            self.VelicinaElite = VelicinaElite
        else:
            raise Exception ("Veličina elite mora biti cijeli broj između 0 i 2.")

    def GetVelicinaElite(self):
        return self.VelicinaElite

    def OpUkrstanjaTacka(self, Roditelj1, Roditelj2):
        v = np.random.uniform(0, 1)
        if self.VjerovatnocaUkrstanja > v:
            print("Fitnessi roditelja su ", Roditelj1.GetFitness(), Roditelj2.GetFitness())
            k = np.random.randint(0, self.DuzinaHromozoma)
            print("Tačka ukrštanja je ", k)
            dijete1 = MojaIndividua(self.DuzinaHromozoma)
            dijete2 = MojaIndividua(self.DuzinaHromozoma)
            niz1 = []
            niz2 = []
            for i in range (0, k):
                niz1.append(Roditelj1.GetHromozom()[i])  # prvo dijete dobija kao prvi dio početak roditelja1
            for i in range (k, self.DuzinaHromozoma):
                niz1.append(Roditelj2.GetHromozom()[i])  # prvo dijete dobija kao drugi dio kraj roditelja2
            for i in range (0, k):
                niz2.append(Roditelj2.GetHromozom()[i])  # drugo dijete dobija kao prvi dio početak roditelja2
            for i in range (k, self.DuzinaHromozoma):
                niz2.append(Roditelj1.GetHromozom()[i])  # drugo dijete dobija kao drugi dio kraj roditelja1
            dijete1.SetHromozom(niz1)
            dijete2.SetHromozom(niz2)
            return dijete1, dijete2
        return None

    def OpUkrstanjaDvijeTacke(self, Roditelj1, Roditelj2):
        v = np.random.uniform(0, 1)
        if self.VjerovatnocaUkrstanja > v:
            while (1):
                k = np.random.randint(0, self.DuzinaHromozoma-1)
                h = np.random.randint(0, self.DuzinaHromozoma)
                if (k < h):
                    break
            print("Tačke ukrštanja su ", k, " i ", h)
            dijete1 = MojaIndividua(self.DuzinaHromozoma)
            dijete2 = MojaIndividua(self.DuzinaHromozoma)
            niz1 = []
            niz2 = []
            for i in range (0, k):
                niz1.append(Roditelj1.GetHromozom()[i])
                niz2.append(Roditelj2.GetHromozom()[i])
            for i in range (k, h):
                niz1.append(Roditelj2.GetHromozom()[i])
                niz2.append(Roditelj1.GetHromozom()[i])
            for i in range (h, self.DuzinaHromozoma):
                niz1.append(Roditelj1.GetHromozom()[i])
                niz2.append(Roditelj2.GetHromozom()[i])
            dijete1.SetHromozom(niz1)
            dijete2.SetHromozom(niz2)
            return dijete1, dijete2
        return None

    def OpBinMutacija(self, H):
        v = np.random.uniform(0, 1)
        if self.VjerovatnocaMutacije > v:
            k = np.random.randint(0, self.DuzinaHromozoma)
            print("Mutacija se dešava na poziciji ", k)
            trenutni = H.GetHromozom()
            if (trenutni[k]):
                trenutni[k] = 0
            else:
                trenutni[k] = 1
            H.SetHromozom(trenutni)
        return H

    def SelekcijaRTocak(self):
        sumaFitnessa = 0
        populacija = self.GetPopulacija()
        for hr in populacija:
            sumaFitnessa += hr.GetFitness()
        p = np.random.uniform(0, 1)
        i = 0
        sumaVjerovatnoca = populacija[i].GetFitness() / sumaFitnessa  #inicijalno ima samo vjerovatnocu prvog hromozoma
        while sumaVjerovatnoca < p:
            i += 1
            sumaVjerovatnoca += populacija[i].GetFitness() / sumaFitnessa
        return i

    def SelekcijaRang(self):
        RANG_SP = 2
        #sortiranje po vrijednosti fitnessa
        populacija = sorted(self.GetPopulacija(), key=lambda x: x.GetFitness(), reverse=False)
        #print("Sortirana populacija je ",)
        #for i in range(0, len(populacija)):
       #     print(populacija[i].GetFitness())
        sumaModFitnessa = 0
        for i in range(0, len(populacija)):
            sumaModFitnessa += (2 - RANG_SP) + 2 * (RANG_SP - 1) * (i - 1) / (self.VelicinaPopulacije - 1)
        p = np.random.uniform(0, 1)
        i = 0
        sumaVjerovatnoca = ((2 - RANG_SP) + 2 * (RANG_SP - 1) * (i - 1) / (self.VelicinaPopulacije - 1)) / sumaModFitnessa
        while sumaVjerovatnoca < p:
            i += 1
            sumaVjerovatnoca += ((2 - RANG_SP) + 2 * (RANG_SP - 1) * (i - 1) / (self.VelicinaPopulacije - 1)) / sumaModFitnessa
        return i

    def NovaGeneracija(self):
        #parametar VelicinaElite koji govori koliko najboljih jedinki se zadrzava
        #kada se ukrste svi, izbacit ćemo dijete s najlošijim fitnessom, a prenijeti najboljeg roditelja
        populacija = self.GetPopulacija()
        novaGeneracija = []
        for i in range(0, int((self.VelicinaPopulacije)//2)):
            prvaJedinka = populacija[self.SelekcijaRTocak()]
            drugaJedinka = populacija[self.SelekcijaRTocak()]
            #prvaJedinka = populacija[self.SelekcijaRang()]
            #drugaJedinka = populacija[self.SelekcijaRang()]
            while (prvaJedinka == drugaJedinka):
                prvaJedinka = populacija[self.SelekcijaRTocak()]
                drugaJedinka = populacija[self.SelekcijaRTocak()]
            print("Jedinke koje se ukrstaju su ", prvaJedinka.GetHromozom(), drugaJedinka.GetHromozom())
            rezultatUkrstanja = self.OpUkrstanjaTacka(prvaJedinka, drugaJedinka)
            if rezultatUkrstanja != None:
                prvoDijete = rezultatUkrstanja[0]
                drugoDijete = rezultatUkrstanja[1]
            else:
                continue
            if prvoDijete != None:
                self.OpBinMutacija(prvoDijete)
                novaGeneracija.append(prvoDijete)
            if drugoDijete != None:
                self.OpBinMutacija(drugoDijete)
                novaGeneracija.append(drugoDijete)
            print("NJihova djeca su ", prvoDijete.GetHromozom(), drugoDijete.GetHromozom())
        for k in range(0, self.VelicinaElite):
            minFitness = novaGeneracija[0].GetFitness()
            j = 0
            for i in range(1, len(novaGeneracija)):
                if novaGeneracija[i].GetFitness() < minFitness:
                    minFitness = novaGeneracija[i].GetFitness()
                    j = i
            print("Iz generacije se izbacuje jedinka ", novaGeneracija[j].GetHromozom(), " jer ima najmanji fitness ", novaGeneracija[j].GetFitness())
            novaGeneracija.pop(j)  #brise jedinku na poziciji j jer ima najmanji fitness
            #ubacivanje najboljeg roditelja
            maxFitness = populacija[0].GetFitness()
            j = 0
            for i in range(1, len(populacija)):
                if populacija[i].GetFitness() > maxFitness:
                    maxFitness = populacija[i].GetFitness()
                    j = i
            novaGeneracija.append(populacija[j])  #ubacujemo najboljeg iz prethodne generacije u sljedecu
            print("U generaciju se prenosi najbolja tačka ", populacija[j].GetTacka(), " jer ima najbolji fitness ", populacija[j].GetFitness())
            populacija.pop(j)  #ovu populaciju cemo svakako zamijeniti novom, a kada izbacimo najbolji, drugi put mozemo pronaci drugi najbolji
        self.SetPopulacija(novaGeneracija)
        return novaGeneracija

    def GenerisiGeneracije(self):
        for i in range(0, self.MaxGeneracija):
            self.NovaGeneracija()
            self.IspisiPopulaciju()
        #ova funkcija vraca maksimalni fitness i tacku koja ima taj max fitness
        populacija = self.GetPopulacija()
        maxFitness = populacija[0].GetFitness()
        j = 0
        for i in range(len(populacija)):
            if populacija[i].GetFitness() > maxFitness:
                maxFitness = populacija[i].GetFitness()
                j = i
        return maxFitness, populacija[j].GetTacka()

    def IspisiPopulaciju(self):
        for i in range(0, len(self.GetPopulacija())):
            print(self.GetPopulacija()[i].GetHromozom())

if __name__ == '__main__':
    try:
        p = Populacija(30, 0.99, 0.01, 50, 1, 20)
        print("Početna populacija je: ")
        p.IspisiPopulaciju()
        #p.GenerisiGeneracije()
        maxFitness, maxTacka = p.GenerisiGeneracije()
        print("Maksimalni fitness je ", maxFitness, " u tački ", maxTacka)

        """
        r1 = np.random.randint(1, p.GetVelicinaPopulacije() - 1)
        p1 = p.GetPopulacija()[r1]
        print(p1.GetHromozom())
        print(p1.Evaluiraj())
        
        r2 = np.random.randint(1, p.GetVelicinaPopulacije() - 1)
        p1 = p.GetPopulacija()[r1]
        p2 = p.GetPopulacija()[r2]
        print("P1", p1.GetHromozom())
        print("P2", p2.GetHromozom())
        (c1, c2) = p.OpUkrstanjaTacka(p1, p2)
        print("C1", c1.GetHromozom())
        print("C2", c2.GetHromozom())
        (c11, c22) = p.OpUkrstanjaDvijeTacke(p1, p2)
        print("C11", c11.GetHromozom())
        print("C22", c22.GetHromozom())
        c3 = p.OpBinMutacija(c1)
        print("C3", c3.GetHromozom(), "C1 nakon mutiranja")
        """

    except Exception as e:
        print(e)
