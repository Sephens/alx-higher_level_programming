const person = {
    name:['Steve', 'Adenux'],
    age:33,
    county:'Kisumu',

    bio: function(){
        console.log('${this.name[0]}${this.name[1]}is${this.age} and comes from ${this.county}');
    }

    
}

const numbers = [2,3,5,6];

const myMap = numbers.map(x => x * 3);

console.log(myMap);