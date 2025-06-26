
import React, { useState } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { List, ShoppingCart, Package, UserPlus } from 'lucide-react';
import LoginForm from '@/components/LoginForm';
import Header from '@/components/Header';
import RequestsTable from '@/components/RequestsTable';
import PurchaseRequestForm from '@/components/PurchaseRequestForm';
import WarehouseRequestForm from '@/components/WarehouseRequestForm';
// import UserRegistrationForm from '@/components/UserRegistrationForm';

interface User {
  id: number;
  name: string;
  email: string;
}

const Index = () => {
  const [user, setUser] = useState<User | null>(null);
  const [activeTab, setActiveTab] = useState('requests');

  const handleLogin = (userData: User) => {
    setUser(userData);
  };

  const handleLogout = () => {
    setUser(null);
    setActiveTab('requests');
  };

  if (!user) {
    return <LoginForm onLogin={handleLogin} />;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header user={user} onLogout={handleLogout} />
      
      <div className="container mx-auto px-4 py-6">
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-2 mb-6"> {/* alterar grid-cols-n para o número correspondente de itens apresentados */}
            <TabsTrigger value="requests" className="flex items-center space-x-2">
              <List className="h-3 w-3" />
              <span className="hidden sm:inline">Lista de Solicitações</span>
              <span className="sm:hidden">Lista</span>
            </TabsTrigger>
            <TabsTrigger value="purchase" className="flex items-center space-x-2">
              <ShoppingCart className="h-3 w-3" />
              <span className="hidden sm:inline">Solicitação de Compras</span>
              <span className="sm:hidden">Compras</span>
            </TabsTrigger>
            {/* <TabsTrigger value="warehouse" className="flex items-center space-x-2">
              <Package className="h-3 w-3" />
              <span className="hidden sm:inline">Solicitação ao Almoxarifado</span>
              <span className="sm:hidden">Almoxarifado</span>
            </TabsTrigger> */}
            {/* <TabsTrigger value="users" className="flex items-center space-x-2">
              <UserPlus className="h-3 w-3" />
              <span className="hidden sm:inline">Cadastrar Usuário</span>
              <span className="sm:hidden">Usuários</span>
            </TabsTrigger> */}
          </TabsList>

          <TabsContent value="requests" className="space-y-4">
            <RequestsTable />
          </TabsContent>

          <TabsContent value="purchase" className="space-y-4">
            <PurchaseRequestForm user={user} />
          </TabsContent>

          {/* <TabsContent value="warehouse" className="space-y-4">
            <WarehouseRequestForm user={user} />
          </TabsContent> */}

          {/* <TabsContent value="users" className="space-y-4">
            <UserRegistrationForm />
          </TabsContent> */}
        </Tabs>
      </div>
    </div>
  );
};

export default Index;
