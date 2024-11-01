import subprocess , shutil , tempfile , os , textwrap




class nim  : 

	@classmethod
	def parse(cls,code , nim = None ) : 
		compiler_nim = nim if nim is not None else shutil.which('nim')
		astresult = None
		with tempfile.NamedTemporaryFile(mode='w+', suffix = '.nim' , delete=True) as temp_file:
			indented_code =  textwrap.indent(code, prefix="    ")
			temp_file.write(f'import macros \n\n\ndumpAstGen : \n{indented_code}\n')
			temp_file.flush()
			#os.system(f'cat {temp_file.name}')
			cmd = [
				compiler_nim , 'r' , '--hints:off' , temp_file.name
			]
			result = subprocess.run(cmd, capture_output=True, text=True)
			if result.returncode != 0 : 
				raise Exception(result.stderr)
			astresult = result.stdout
		return astresult.strip()
	@classmethod
	def unparse(cls,code , nim = None ) : 
		compiler_nim = nim if nim is not None else shutil.which('nim')
		astresult = None
		with tempfile.NamedTemporaryFile(mode='w+', suffix = '.nim' , delete=True) as temp_file:
			indented_code =  textwrap.indent(code, prefix="    ")
			temp_file.write(f'import macros\n\n\nmacro TreeGeneration(): untyped =\n  let tree = {indented_code}\n  echo tree.repr\n\nTreeGeneration()\n')
			temp_file.flush()
			cmd = [
				compiler_nim , 'r' , '--hints:off' , temp_file.name
			]
			result = subprocess.run(cmd, capture_output=True, text=True)
			if result.returncode != 0 : 
				raise Exception(result.stderr)
			astresult = result.stdout
		return astresult.strip()



