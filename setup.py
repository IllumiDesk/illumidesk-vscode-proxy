import setuptools

setuptools.setup(
    name="illumidesk-vscode-proxy",
    version='0.1.0',
    url="https://github.com/jupyterhub/illumidesk-vscode-proxy",
    author="IllumiDesk Team",
    description="hello@illumidesk.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter', 'IllumiDesk', 'VS Code'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'vscode = illumidesk_vscode_proxy:setup_vscode',
        ]
    },
    package_data={
        'illumidesk_vscode_proxy': ['icons/*'],
    },
)
