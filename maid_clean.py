import os
import shutil
import subprocess
import fire

class MaidClean:
    @staticmethod
    def remove_pycache(directory='.'):
        """Remove todos os diretórios __pycache__ e arquivos .pyc"""
        for root, _, files in os.walk(directory):
            if root.endswith('__pycache__'):
                # Primeiro, remover os arquivos .pyc dentro da pasta
                for f in files:
                    file_path = os.path.join(root, f)
                    if os.path.exists(file_path) and f.endswith('.pyc'):
                        os.remove(file_path)
                        print(f'Removido arquivo .pyc: {file_path}')

                # Depois, remover o diretório __pycache__ se ele ainda existir
                if os.path.exists(root):
                    shutil.rmtree(root)
                    print(f'Removido diretório __pycache__: {root}')

    @staticmethod
    def remove_node_modules(directory='.'):
        """Remove todos os diretórios node_modules"""
        for root, dirs, _ in os.walk(directory):
            if 'node_modules' in dirs:
                node_modules_path = os.path.join(root, 'node_modules')
                shutil.rmtree(node_modules_path)
                print(f'Removido diretório node_modules: {node_modules_path}')

    @staticmethod
    def clean_flutter(directory='.'):
        """Executa 'flutter clean' em projetos Flutter detectados"""
        for root, _, files in os.walk(directory):
            if 'pubspec.yaml' in files:
                try:
                    subprocess.run(["flutter", "clean"], cwd=root)
                    print(f'Executado "flutter clean" em: {root}')
                except Exception as e:
                    print(f'Erro ao executar "flutter clean" em {root}. Razão: {e}')

    @staticmethod
    def all(directory='.'):
        """Executa todas as operações de limpeza"""
        MaidClean.remove_pycache(directory)
        MaidClean.remove_node_modules(directory)
        MaidClean.clean_flutter(directory)

def main():
    fire.Fire(MaidClean)

if __name__ == '__main__':
    main()
