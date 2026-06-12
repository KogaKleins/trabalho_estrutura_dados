from services.cores import VERMELHO, VERDE, RESET
class DeleteAluno:

    def __init__(self, sala, aluno):
        self.aluno = aluno
        self.sala = sala


    def remove_aluno(self):
            
            while True:

                confirma = input (f"{VERMELHO}Tem certeza que deseja excluir o aluno? S/N: {RESET}").strip().upper()

                if confirma == "S" or confirma == "N":
                        break
                else:
                    print ("Apenas S ou N ")
                                
            if confirma == "S":

                self.sala.sala_aula.remove(self.aluno)
                print (f"{VERDE}Aluno removido com sucesso! {RESET} ")
            else:
                  return 
                  


        