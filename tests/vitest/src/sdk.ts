import { execFile } from 'node:child_process'
import { createHash } from 'node:crypto'
import { existsSync, readdirSync, readFileSync } from 'node:fs'
import path from 'node:path'
import { promisify } from 'node:util'

const run = promisify(execFile)

export const REPO_ROOT = path.resolve(__dirname, '../../..')
const PROBE = path.join(REPO_ROOT, 'tests/vitest/harness/probe.py')

export interface SdkPackage {
  name: string
  dir: string
  requirements: string
  requirementsHash: string
}

/** Every generated package: a top-level directory with setup.py and requirements.txt. */
export function listPackages(): SdkPackage[] {
  return readdirSync(REPO_ROOT, { withFileTypes: true })
    .filter((d) => d.isDirectory() && !d.name.startsWith('.') && d.name !== 'tests')
    .map((d) => path.join(REPO_ROOT, d.name))
    .filter((dir) => existsSync(path.join(dir, 'setup.py')) && existsSync(path.join(dir, 'requirements.txt')))
    .map((dir) => {
      const requirements = path.join(dir, 'requirements.txt')
      const requirementsHash = createHash('sha256').update(readFileSync(requirements)).digest('hex').slice(0, 12)
      return { name: path.basename(dir), dir, requirements, requirementsHash }
    })
    .sort((a, b) => a.name.localeCompare(b.name))
}

/** Endpoints documented in the package README ("Documentation for API Endpoints" table). */
export function documentedEndpoints(pkg: SdkPackage): { api: string; method: string; verb: string; route: string }[] {
  const readme = readFileSync(path.join(pkg.dir, 'README.md'), 'utf8')
  const row = /^\*(\w+)\* \| \[\*\*(\w+)\*\*\]\([^)]*\) \| \*\*(\w+)\*\* ([^ |]+)/gm
  return [...readme.matchAll(row)].map((m) => ({ api: m[1], method: m[2], verb: m[3].toUpperCase(), route: m[4] }))
}

export async function probe(python: string, args: string[]): Promise<any> {
  const { stdout } = await run(python, [PROBE, ...args], { cwd: REPO_ROOT, maxBuffer: 16 * 1024 * 1024 })
  return JSON.parse(stdout)
}
