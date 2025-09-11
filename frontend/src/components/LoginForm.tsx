import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";

import { jwtDecode } from "jwt-decode";

interface User {
  id: number;
  name: string;
  email: string;
  nome: string;
  sobrenome: string;
}

interface LoginFormProps {
  onLogin: (userData: User) => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ onLogin }) => {
  const [username, setUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);
    try {
      // Simulação de API de login - substitua pela sua API real
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),
      });

      if (response.ok) {
        const userData = await response.json();
        const decoded: any = jwtDecode(userData.access_token);

        // Salva o token e os dados do usuário
        localStorage.setItem("token", userData.access_token);
        localStorage.setItem("user", JSON.stringify({
          nome: decoded.nome,
          sobrenome: decoded.sobrenome
        }));

        onLogin({
          id: decoded.id || 0,
          name: decoded.nome || '',
          email: decoded.email || '',
          nome: decoded.nome,
          sobrenome: decoded.sobrenome
        });
        toast({
          title: "Login realizado com sucesso!",
          description: `Bem-vindo, ${decoded.nome || "usuário"}!`,
        });
      } else {
        throw new Error('Credenciais inválidas');
      }
    } catch (error) {
      // console.log(error)
      toast({
        title: "Erro",
        description: `${error}`,
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
                value={username}
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
