import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { PitagorasService } from '../pitagoras.service';
import { FormsModule } from '@angular/forms'

@Component({
  selector: 'app-calculadora',
  templateUrl: './calculadora.component.html',
  styleUrls: ['./calculadora.component.css'],
})
export class CalculadoraComponent {
  msg_error=null;
  menu=['Hipotenusa', 'Catetos']
  opt_menu='';
  valores: any={
    a: '',
    b: '',
    c: ''
  }
  

  constructor(private pitagorasService: PitagorasService) {}


  onSubmit(){
    
    this.valores.c = null;
    this.msg_error = null;
  
    if (this.opt_menu == 'Hipotenusa'){
      this.pitagorasService.calcular_hipotenusa(this.valores.a, this.valores.b).subscribe(
        (resultado: any) => {
          this.valores.c = resultado['valor_c'];
          this.msg_error = null;
        },
        (error) => {
          this.msg_error = error.error;
          this.valores.c = null;
        }
      ); 
    }
    
    else if (this.opt_menu == 'Catetos'){
      this.pitagorasService.calcular_cateto(this.valores.a, this.valores.b).subscribe(
        (resultado: any) => {
          this.valores.c = resultado['valor_c'];
          this.msg_error = null;
        },
        (error) => {
          this.msg_error = error.error;
          this.valores.c = null;
        }
      ); 
    }
    
}
}
