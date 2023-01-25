import { Component, Input, OnInit } from '@angular/core';
import { PitagorasService } from '../pitagoras.service';
import { FormsModule } from '@angular/forms'

@Component({
  selector: 'app-calculadora',
  templateUrl: './calculadora.component.html',
  styleUrls: ['./calculadora.component.css'],
})
export class CalculadoraComponent implements OnInit {
  msg_resultado=''
  valores: any={
    a: '',
    b: '',
    c: ''
  }
  

  constructor(private pitagorasService: PitagorasService) {}

  ngOnInit(): void {
    console.log('CarregueiOnInit');
    
  }
  onSubmit(){
    console.log('CarregueiSubmit')
    console.log(this.valores)
    this.pitagorasService.calcular(this.valores.a, this.valores.b).subscribe(
      (resultado) => {
        console.log(this.valores.c)
        this.valores = resultado
       
      },
      (error) => {
        console.log('Error' + error.error);
      }
    );
}
}
