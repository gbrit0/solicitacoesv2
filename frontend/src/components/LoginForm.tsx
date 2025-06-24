import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";

interface LoginFormProps {
  onLogin: (userData: { id: number; name: string; email: string }) => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ onLogin }) => {
  const [usuario, setUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Simulação de API de login - substitua pela sua API real
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ usuario, password }),
      });

      if (response.ok) {
        const userData = await response.json();
        onLogin(userData);
        toast({
          title: "Login realizado com sucesso!",
          description: `Bem-vindo, ${userData.name}!`,
        });
      } else {
        throw new Error('Credenciais inválidas');
      }
    } catch (error) {
      // Para demonstração, vou simular um login bem-sucedido
      console.log('Simulando login para demonstração');
      const mockUser = {
        id: 1,
        name: 'Gabriel Brito Ribeiro',
        email: usuario || 'usuario@exemplo.com'
      };
      onLogin(mockUser);
      toast({
        title: "Login realizado com sucesso!",
        description: `Bem-vindo, ${mockUser.name}!`,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#0d4b28]">
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
        <div className="flex items-center justify-center w-full space-x-4">
          <img src="/logo.png" alt="Logo" className="h-10 w-auto" />
          <CardTitle className="text-2xl text-center text-green-700">Sistema de Solicitações</CardTitle>
          {/* <h1 className="text-2xl font-bold">Sistema de Solicitações</h1> */}
        </div>
          <CardDescription className="text-center">
            Faça login com as credenciais do GLPI para acessar o sistema
          </CardDescription>
        </CardHeader>
        <form onSubmit={handleLogin}>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="usuario">Usuário</Label>
              <Input
                id="usuario"
                type="text"
                placeholder="joao.silva"
                value={usuario}
                onChange={(e) => setUsuario(e.target.value)}
                required
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Senha</Label>
              <Input
                id="password"
                type="password"
                placeholder="Sua senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
          </CardContent>
          <CardFooter>
            <Button type="submit" className="w-full bg-green-600 hover:bg-green-700" disabled={loading}>
              {loading ? 'Entrando...' : 'Entrar'}
            </Button>
          </CardFooter>
        </form>
      </Card>
    </div>
  );
};

export default LoginForm;
