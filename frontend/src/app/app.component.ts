import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  date=new Date().toDateString(); //to display date in day-month-date-year format
 
  
  displaycity:String = "";  
  city: String = "";
  isDisplay = true;
  temp:any;  //variabale to check the cod 
  toggleDisplay() {
    if (this.city != "") {
      this.displaycity = this.city;
      this.http.post("http://127.0.0.1:8000/", { 'city': this.city }).subscribe(data => {
        this.temp=data
        if(this.temp.cod=="404"){    //checking whether the given city is valid or not
        this.isDisplay=true;
        alert("Enter valid city name")
        }
        else if(this.temp.cod=="405"){  //checking whether the city name is numbers
          this.isDisplay=true;
         alert("City name should not contain numbers")
        }
        else{
          this.isDisplay = false;
          this.weatherdata = data;
        }   
      }
      )
      this.http.post("http://127.0.0.1:8000/forecast/", { 'city' : this.city }).subscribe(data => {
        this.forecastdata = data;
        // The data contains a cod for api status, so reducing the length by one
        this.forecastdata.splice(this.forecastdata.length-1,this.forecastdata.length-1)
      })
    }
    else {
      
      alert("City name should not be empty")
    }
  }
  constructor(private http: HttpClient) { }

  weatherdata: any = {
    "weather_condition": "",
    "temperature": 0,
    "city": "",
    "humidity": 0,
    "pressure": 0,
    "minimum_temp": 0,
    "maximum_temp": 0,
    "icon": ""
  }
  forecastdata:any;
  
sort(){
  this.forecastdata.reverse()  //to reverse the dates in the forcast data
}

  ngOnInit(): void {

  }

}
