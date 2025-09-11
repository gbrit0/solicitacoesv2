import React from 'react';
import { useAuth } from '@/hooks/useAuth';
import LoginForm from '@/components/LoginForm';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { isAuthenticated, isLoading, login } = useAuth();

  // Mostrar loading enquanto verifica autenticação
  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#0d4b28]">
        <div className="text-white text-lg">Carregando...</div>
      </div>
    );
  }

  // Se não estiver autenticado, mostrar formulário de login
  if (!isAuthenticated) {
    return <LoginForm onLogin={login} />;
  }

  // Se estiver autenticado, mostrar o conteúdo protegido
  return <>{children}</>;
};

export default ProtectedRoute;
