
#include <cstdlib>
#include <vector>
#include <iostream>
#include <array>
#include <string>
#include <cmath>
#include "ConsoleColor.h"

using namespace std;

array<string, 117> elements =
{
	"Aluminium",
	"Americium",
	"Argon",
	"Arsenic",
	"Astatine",
	"Barium",
	"Berkelium",
	"Beryllium",
	"Bismuth",
	"Bohrium",
	"Boron",
	"Bromine",
	"Cadmium",
	"Caesium",
	"Calcium",
	"Californium",
	"Carbon",
	"Cerium",
	"Chlorine",
	"Chromium",
	"Cobalt",
	"Copernicium",
	"Copper",
	"Curium",
	"Darmstadtium",
	"Dubnium",
	"Dysprosium",
	"Einsteinium",
	"Erbium",
	"Europium",
	"Fermium",
	"Flerovium",
	"Fluorine",
	"Francium",
	"Gadolinium",
	"Gallium",
	"Germanium",
	"Gold",
	"Hafnium",
	"Hassium",
	"Helium",
	"Holmium",
	"Hydrogen",
	"Indium",
	"Iodine",
	"Iridium",
	"Iron",
	"Krypton",
	"Lanthanum",
	"Lawrencium",
	"Lead",
	"Lithium",
	"Livermorium",
	"Lutetium",
	"Magnesium",
	"Manganese",
	"Meitnerium",
	"Mendelevium",
	"Mercury",
	"Molybdenum",
	"Moscovium",
	"Neodymium",
	"Neon",
	"Neptunium",
	"Nickel",
	"Nihonium",
	"Niobium",
	"Nitrogen",
	"Nobelium",
	"Oganesson",
	"Osmium",
	"Oxygen",
	"Palladium",
	"Phosphorus",
	"Platinum",
	"Plutonium",
	"Polonium",
	"Potassium",
	"Praseodymium",
	"Promethium",
	"Protactinium",
	"Radium",
	"Radon",
	"Rhenium",
	"Rhodium",
	"Roentgenium",
	"Rubidium",
	"Ruthenium",
	"Rutherfordium",
	"Samarium",
	"Samarium",
	"Scandium",
	"Seaborgium",
	"Selenium",
	"Silicon",
	"Silver",
	"Sodium",
	"Strontium",
	"Sulfur",
	"Tantalum",
	"Technetium",
	"Tellurium",
	"Tennessine",
	"Terbium",
	"Thallium",
	"Thorium",
	"Thulium",
	"Tin",
	"Titanium",
	"Tungsten",
	"Uranium",
	"Vanadium",
	"Xenon",
	"Ytterbium",
	"Yttrium",
	"Zinc",
	"Zirconium"
};

// ideally, a hashtable should be approximately
// 25% larger than the data set
const unsigned TABLE_SIZE = elements.size() * 1.25f;
static int maximum = TABLE_SIZE;

int HashMultiplicative(string key)
{
	int sum = key[0] - 'A' + 1;
	for (int c = 1; c < key.length(); c++)
		sum += (key[c] - 'a' + 1);
	int HashMultiplier = 709; // prime
	int stringHash = key[0] - 'A' + 1;
	for (int c = 0; c < key.length(); c++)
		stringHash += (sum * HashMultiplier) + (key[c] - 'a' + 1);
	return stringHash % maximum;
}

int HashMidSquare(string key)
{
	int sum = key[0] - 'A' + 1;
	for (int c = 1; c < key.length(); c++)
		sum += (key[c] - 'a' + 1);
	int squaredKey = sum * sum;
	int R = (log(sum) / log(2));
	int lowBitsToRemove = (32 - R) / 2;
	int extractedBits = squaredKey >> lowBitsToRemove;
	extractedBits = extractedBits & (0xFFFFFFFF >> (32 - R));
	return extractedBits % maximum;
}

int HashRemainder(string key)
{
	int sum = key[0] - 'A' + 1;
	for (int c = 1; c < key.length(); c++)
		sum += (key[c] - 'a' + 1);
	return sum % maximum;
}

int HashOddEven(string key)
{
	int sum = key[0] - 'A' + 1;
	for (int c = 1; c < key.length(); c++)
	{
		if (c % 2 == 1)
			sum += (key[c] - 'a' + 1);
		else
			sum += ((key[c] - 'a' + 1) * 2);
	}
	return sum % maximum;
}

// a good hashing function returns few collisions
int getHash(string key)
{
	//return HashMultiplicative(key);
	//return HashMidSquare(key);
	//return HashRemainder(key);
	return HashOddEven(key); 
}


class HashElement 
{
private:
      int key = 0;
      string value = "";
	  LinkedList dll = DLL() 
public:
	  int used = 0;
	  // used keeps track of how many times it gets set
      HashElement(int k=0, string v="",int u=0) 
	  {
            key = k;
            value = v;
			used = u;
      }
	  void setKeyValue(int k, string v)
	  {
		  key = k;
		  value = v;
		  used++;
	  }
      int getKey() 
	  {	
            return key;
      }
      string getValue() 
	  {
            return value;
      }
	  operator int() { return getKey(); }
};

class HashTable 
{
private:
      vector<HashElement> table;
	  int collisions = 0;
public:
	HashTable(int s = 1) { table.resize(s); }
	int size() { return table.size(); }
	int getcollisions() { return collisions; }
	string get(string key) 
	{
		int hash = getHash(key);
		return table[hash].getValue();
	}
	HashElement get(int index)
	{
		return table[index];
	}
	void set(string value) 
	{
		// value == "Titanium"
		int hash = getHash(value);
		// 1. create hash from getHash 
		HashElement element;
		element.setKeyValue(hash, value);
		// 2. create hashelement and then pass the hashed integer and value into the hash element
		// the key itself is the hash, the value is the value passed in
		// each hashelement only contains a single key and a single value
		int key = table[hash].getKey();
		// if key already existed, as in table[19].getKey() 
		if (key > 0)
		{
			table[hash].dll.Append(value)
			collisions++;
			element.used++;
		}
		// then just overwrite
		table[hash] = element;
	}     
	HashElement operator [] (int index)
	{
		return get(index);
	}
};  

void main()
{
	HashTable htable(TABLE_SIZE);
	for (int x=0; x<elements.size(); x++)
		htable.set(elements[x]);
	int used = 0;
	for (int x = 0; x < htable.size(); x++)
	{
		HashElement hentry = htable.get(x);
		if (hentry.getKey() > 0)
		{
			used++;
			if (hentry.used > 1)
			{
				cout << red << "\n[" << hentry.getKey() << "] " << '\t' << hentry.getValue();
			}
			else
				cout << green << "\n[" << hentry.getKey() << "] " << '\t' << hentry.getValue();
		}
		else
			cout << blue << ".";
	}
	cout << yellow;
	cout << "\nStatistics:" << endl;
	cout << "\tMaximum = " << maximum << endl;
	// maximum = size of hash table
	cout << "\tUsed = " << (float)used / (float)htable.size()*100.0 << "%" << endl;
	// used = 
	cout << "\tCollisions = " << float(htable.getcollisions()) / float(elements.size()) * 100.0 << "%" << endl;
}