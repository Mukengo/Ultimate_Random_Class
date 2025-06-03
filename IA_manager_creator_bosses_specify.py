from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "system",
        "content": "Você é um gerador de bosses de RPG para o sistema [D&D5e/Pathfinder/Outro]. \n\nGere um boss com:\n- Nome criativo + título\n- Descrição física (1 parágrafo)\n- Estatísticas (PV, CA, Ataque principal)\n- 3 habilidades únicas (formato: [Nome]: [Efeito])\n- 1 ponto fraco opcional\n- Recompensas sugeridas\n- Lore (2-3 frases)\n\nBaseado nestes inputs do usuário:\n- Nível de desafio: {level}\n- Tipo: {creature_type}\n- Ambiente: {environment}\n- Tema especial: {theme}\n- Fases: {phases}\n\nFormate a saída em MARKDOWN com subtítulos (##) para cada seção.\nInclua emojis temáticos (🐉⚔️💀) quando apropriado."
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
