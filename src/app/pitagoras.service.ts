import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class PitagorasService {
  constructor(private httpclient: HttpClient) {}
  
  calcular(a: number, b: number) {
    return this.httpclient.post('http://localhost:5000/calculator', {
      a: a,
      b: b,
    });
  }
  ca(a: number, b: number) {
    return this.httpclient.post('http://localhost:5000/ca', {
      a: a,
      b: b,
    });
  }
}
