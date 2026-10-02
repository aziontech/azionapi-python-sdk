import { execFileSync } from 'node:child_process'
import { existsSync, mkdirSync } from 'node:fs'
import path from 'node:path'
import type { TestProject } from 'vitest/node'
import { listPackages, REPO_ROOT } from './src/sdk'

// One virtualenv per distinct requirements.txt: the packages were produced by
// different generator versions whose requirements conflict (pydantic 1 vs 2).
export async function setup(project: TestProject): Promise<void> {
  const python = process.env.PYTHON ?? 'python3'
  const venvRoot = process.env.SDK_VENV_DIR ?? path.join(REPO_ROOT, 'tests/vitest/.venvs')
  mkdirSync(venvRoot, { recursive: true })

  const interpreters: Record<string, string> = {}
  for (const pkg of listPackages()) {
    const venv = path.join(venvRoot, pkg.requirementsHash)
    const bin = path.join(venv, process.platform === 'win32' ? 'Scripts/python.exe' : 'bin/python')
    if (!existsSync(bin)) {
      execFileSync(python, ['-m', 'venv', venv], { stdio: 'inherit' })
      execFileSync(bin, ['-m', 'pip', 'install', '--quiet', '--disable-pip-version-check', '-r', pkg.requirements], {
        stdio: 'inherit',
      })
    }
    interpreters[pkg.name] = bin
  }
  project.provide('interpreters', interpreters)
}

declare module 'vitest' {
  export interface ProvidedContext {
    interpreters: Record<string, string>
  }
}
