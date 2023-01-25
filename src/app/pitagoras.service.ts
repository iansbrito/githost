import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class PitagorasService {
  constructor(private httpclient: HttpClient) {}

  api_url = 'https://iansbritoti.pythonanywhere.com/calculator'
  
  calcular_hipotenusa(a: number, b: number) {
    return this.httpclient.post(`${this.api_url}/hipotenusa`, {
      a: a,
      b: b,
    });
  }
  calcular_cateto(a: number, b: number) {
    return this.httpclient.post(`${this.api_url}/cateto`, {
      a : a,
      b: b,
    });
  }
}
