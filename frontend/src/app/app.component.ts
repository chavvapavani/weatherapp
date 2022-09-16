import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  displaycity: String = "";
  city: String = "";
  isDisplay = true;
  toggleDisplay() {
    if (this.city != "") {
      this.isDisplay = false;
      this.displaycity = this.city;
      this.http.post("http://127.0.0.1:8000/", { 'city': this.city }).subscribe(data => {
        this.weatherdata = data;
        console.log("pavani", data, this.weatherdata);
      }
      )
    }
    else {
      this.isDisplay = true;
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
  link = "http://openweathermap.org/img/wn/10d@2x.png";

  send_data = {
    "city": this.city
  }

  ngOnInit(): void {

  }
}
